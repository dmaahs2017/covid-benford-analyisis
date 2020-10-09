import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

def read_data(file, columns):
    data = pd.read_csv("all-states-history.csv")
    return data[columns]

def leading_digit(number):
    try:
        while number >= 10 or number <= -10:
            number = number / 10
        return int(math.floor(abs(number)))
    except ValueError:
        return np.nan # -1 means no data was reported for this state on this day


def process_column(col, fn):
    return [fn(el) for el in col]

def logRecip(number):
    return 0-math.log(1 / ( number + 1 ))

def analyse(data_, column):
    data["leading_digit"] = process_column(data[column], leading_digit)
    freq = pd.DataFrame()

    freq["count"] = data["leading_digit"].value_counts(dropna=True)
    freq.index = process_column(freq.index, int)
    freq = freq.drop(0)
    freq["freq"] = freq["count"] / freq["count"].sum()
    freq["log_freq"] = process_column(freq.freq, logRecip)
    return (freq, freq["count"].sum())

def graph(freq_table, col):
    plt.bar(freq_table.index, freq_table.freq)
    plt.title(col)
    plt.xlabel("digits")
    plt.ylabel("freq")
    plt.savefig(f"plots/{col}_bar.png")
    plt.clf()

if __name__ == "__main__":
    data = pd.read_csv("all-states-history.csv")
    for col in data:
        if col in ["positive", "death", "deathIncrease", "positiveCasesViral", "deathConfirmed", "deathProbable"]:
            (freq, total) = analyse(data, col)
            print("=================")
            print(f"{col}, Total: {total}")
            print(freq.shape)
            print(freq)
            print("=================\n")
            graph(freq, col)
