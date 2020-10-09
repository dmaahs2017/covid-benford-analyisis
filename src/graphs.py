import matplotlib.pyplot as plt
import numpy as np
import utils

def display_freq(freq_tables):
    for (table_name, table) in freq_tables:
        print("===============================================================")
        print(f"Table Name: {table_name}, Total Count: {table['count'].sum()}")
        print("===============================================================")
        print(table)
        print("===============================================================")
        print("")

def graph_freq(freq_tables, show=False, export=True, export_to="../plots/frequency_graphs"):
    fig, axs = plt.subplots(2, int(len(freq_tables) / 2))
    fig.suptitle("Frequency of Digit Plots")

    for ((table_name, table), ax) in zip(freq_tables, utils.flatten(axs)):
        ax.bar(table.digit, table.freq)
        ax.set_title(table_name)
        ax.set_xlabel("digits")
        ax.set_ylabel("freq")
        ax.label_outer()
        ax.set_xticks(np.arange(1, 10, step=1))
        ax.set_yticks(np.arange(0, .4, step=.05))

    if export:
        fig.savefig(f"{export_to}.png")
        fig.savefig(f"{export_to}.pdf")
    if show:
        plt.show()
