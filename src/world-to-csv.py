import pandas as pd
import analysis as an

def cumulative(data, path):
    cols = [' New_cases', ' Cumulative_cases', ' New_deaths', ' Cumulative_deaths']
    analysis = [an.analyse(data, col) for col in cols]
    with pd.ExcelWriter(path) as writer:
        pd.DataFrame().to_excel(writer)

    with pd.ExcelWriter(path, mode='a') as writer:
        for col, freq in analysis:
            header = pd.DataFrame()
            header["title"] = [col]
            if len(freq["digit"] > 0):
                header.to_excel(writer, index=False, sheet_name=col, startcol=0)
                freq.to_excel(writer, sheet_name=col, startcol=1)



def indiv_countries(data, path):
    country_col = " Country_code"
    countries = data[country_col].unique()
    cols = [' New_cases', ' Cumulative_cases', ' New_deaths', ' Cumulative_deaths']
    with pd.ExcelWriter(path) as writer:
        pd.DataFrame().to_excel(writer)

    progress = 0
    for country in countries:
        country_data = data[data[country_col] == country]

        analysis = [an.analyse(country_data, col) for col in cols]

        i = 0
        with pd.ExcelWriter(path, mode='a') as writer:
            for col, freq in analysis:
                header = pd.DataFrame()
                header["title"] = [col]
                if len(freq["digit"] > 0):
                    header.to_excel(writer, index=False, sheet_name=country, startcol=0, startrow=i)
                    freq.to_excel(writer, sheet_name=country, startcol=1, startrow=i)
                i += 10
        progress += 1
        print(f"Progress: {( progress / len(countries) * 100 ):.2f}%\t\tCountries: {progress} / {len(countries)}")

def main():
    data = pd.read_csv("../outfiles/data/WHO-COVID-19-global-data.csv")
    cumulative(data, "../outfiles/world_data_report.xlsx")
    indiv_countries(data, "cumulative_world_data_report.xlsx")

if __name__ == "__main__":
    main()
