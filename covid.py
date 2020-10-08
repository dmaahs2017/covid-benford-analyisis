import pandas as pd
import matplotlib as mpl
import numpy as np
import math

def read_data(file, columns):
    data = pd.read_csv("all-states-history.csv")
    return data[columns]

def leading_digit(number):
    try:
        while number >= 10 or number <= -10:
            number = number / 10
        return int(math.floor(number))
    except ValueError:
        return np.nan # -1 means no data was reported for this state on this day


def process_column(col, fn):
    return [fn(el) for el in col]

def analyse(data_, column):
    data["leading_digit"] = process_column(data[column], leading_digit)
    freq = pd.DataFrame()

    freq["count"] = data["leading_digit"].value_counts(dropna=True)
    freq["freq"] = freq["count"] / freq["count"].sum()
    freq.index = process_column(freq.index, int)
    return (freq, freq["count"].sum())

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
