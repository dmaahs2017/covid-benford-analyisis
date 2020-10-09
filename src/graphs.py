import matplotlib.pyplot as plt
import numpy as np
import utils
import os
import math

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
    rows = int(math.sqrt(len(freq_tables)))
    cols = math.ceil(len(freq_tables) / rows)

    fig, axs = plt.subplots(rows, cols)
    fig.suptitle(title)

    try:
        for ((table_name, table), ax) in zip(freq_tables, utils.flatten(axs)):
            ax.bar(table.digit, table.freq)
            ax.set_title(table_name)
            ax.set_xlabel("digits")
            ax.set_ylabel("freq")
            ax.label_outer()
            ax.set_xticks(np.arange(1, 10, step=1))
            ax.set_yticks(np.arange(0, .4, step=.05))
    except TypeError: # axs is just one plot
        for (table_name, table) in freq_tables:
            axs.bar(table.digit, table.freq)
            axs.set_title(table_name)
            axs.set_xlabel("digits")
            axs.set_ylabel("freq")
            axs.label_outer()
            axs.set_xticks(np.arange(1, 10, step=1))
            axs.set_yticks(np.arange(0, .4, step=.05))


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

    plt.close(fig)
