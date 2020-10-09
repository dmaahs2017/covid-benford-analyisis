import pandas as pd
import numpy as np
import math

def process_column(col, fn):
    return [fn(el) for el in col]

def logRecip(number):
    return 0-math.log(1 / ( number + 1 ))

def leading_digit(number):
    try:
        while number >= 10 or number <= -10:
            number = number / 10
        return int(math.floor(abs(number)))
    except ValueError:
        return np.nan # -1 means no data was reported for this state on this day

def analyse(data, column):
    data["leading_digit"] = process_column(data[column], leading_digit)
    freq = pd.DataFrame()

    freq["count"] = data["leading_digit"].value_counts(dropna=True)
    freq.index = process_column(freq.index, int)
    freq = freq.drop(0)
    freq["freq"] = freq["count"] / freq["count"].sum()
    freq["log_freq"] = process_column(freq.freq, logRecip)
    return freq
