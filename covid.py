import pandas as pd
import matplotlib
import graphs
import analysis as an

if __name__ == "__main__":
    data = pd.read_csv("all-states-history.csv")
    columns = ["positive", "death", "deathIncrease", "positiveCasesViral", "deathConfirmed", "deathProbable"]
    freq_data = [an.analyse(data, col) for col in data if col in columns]
    graphs.graph_freq(freq_data, columns)

