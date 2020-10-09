import matplotlib.pyplot as plt
import numpy as np
import utils
import os

def display_freq(freq_tables, filter=""):
    for (table_name, table) in freq_tables:
        print("===============================================================")
        if filter == "":
            print(f"Table Name: {table_name}, Total Count: {table['count'].sum()}")
        else:
            print(f"Table Name: {table_name}, {filter}, Total Count: {table['count'].sum()}")
        print("===============================================================")
        print(table)
        print("===============================================================")
        print("")

def graph_freq(freq_tables, title="Frequency of Digit Plots", show=False, export=True, export_path=".", export_to="digit"):
    fig, axs = plt.subplots(2, int(len(freq_tables) / 2))
    fig.suptitle(title)

    for ((table_name, table), ax) in zip(freq_tables, utils.flatten(axs)):
        ax.bar(table.digit, table.freq)
        ax.set_title(table_name)
        ax.set_xlabel("digits")
        ax.set_ylabel("freq")
        ax.label_outer()
        ax.set_xticks(np.arange(1, 10, step=1))
        ax.set_yticks(np.arange(0, .4, step=.05))

    if export:
        try:
            fig.savefig(f"../plots/{export_path}/{export_to}_freq.png")
            fig.savefig(f"../plots/{export_path}/{export_to}_freq.pdf")
        except FileNotFoundError:
            os.mkdir(f"../plots/{export_path}")
            fig.savefig(f"../plots/{export_path}/{export_to}_freq.png")
            fig.savefig(f"../plots/{export_path}/{export_to}_freq.pdf")
    if show:
        plt.show()
