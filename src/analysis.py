import pandas as pd
import numpy as np
import math
import graphs

def process_column(col, fn):
    return [fn(el) for el in col]

def leading_digit(number):
    try:
        while number >= 10 or number <= -10:
            number = number / 10
        return int(math.floor(abs(number)))
    except ValueError:
        return np.nan # -1 means no data was reported for this state on this day

def analyse(my_data, column):
    data = pd.DataFrame()
    data[column] = my_data[column]
    data["leading_digit"] = process_column(my_data[column], leading_digit)
    freq = pd.DataFrame()

    freq["count"] = data["leading_digit"].value_counts(dropna=True)
    freq.index = process_column(freq.index, int)
    try:
        freq = freq.drop(0)
    except:
        pass
    freq["freq"] = freq["count"] / freq["count"].sum()
    freq["digit"] = freq.index
    return (column, freq)
