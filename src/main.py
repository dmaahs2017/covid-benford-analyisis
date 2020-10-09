import pandas as pd
import graphs
import analysis as an

if __name__ == "__main__":
    data = pd.read_csv("../data/all-states-history.csv")
    columns = ["positive", "death", "deathIncrease", "positiveCasesViral", "deathConfirmed", "deathProbable"]
    states = data["state"].unique()
    freq_data = [an.analyse(data, col) for col in columns]
    graphs.graph_freq(freq_data, title="Frequency of Digits for US", export_path="USA")

    for state in states:
        state_data = data[data["state"] == state]
        state_freq_data = [an.analyse(state_data, col) for col in columns]

        graphs.graph_freq(state_freq_data, title=f"Frequency of Digits for {state}", export_path=state)
        # graphs.display_freq(state_freq_data, filter=f"State: {state}")
