import pandas as pd
import matplotlib as mpl
import numpy as np
import math

def read_data(file, columns):
    data = pd.read_csv("all-states-history.csv")
    return data[columns]

def leading_digit(number):
    try:
        while number >= 10:
            number = number / 10
        return int(math.floor(number))
    except ValueError:
        return -1 # -1 means no data was reported for this state on this day


def process_column(col, fn):
    return [fn(el) for el in col]

if __name__ == "__main__":
    data = read_data("all_states-history.csv", ["state", "date", "positive"])
    data["leading_digit"] = process_column(data["positive"], leading_digit)
    freq = pd.DataFrame(data["leading_digit"].value_counts(), columns = ["Digits", "count"])

