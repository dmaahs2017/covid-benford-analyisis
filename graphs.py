import matplotlib.pyplot as plt
import numpy as np
import utils

def graph_freq(freq_tables, cols):
    fig, axs = plt.subplots(2, int(len(freq_tables) / 2))
    fig.suptitle("Frequency of Digit Plots")
    for (table, col, ax) in zip(freq_tables, cols, utils.flatten(axs)):
        ax.bar(table.index, table.freq)
        ax.set_title(col)
        ax.set_xlabel("digits")
        ax.set_ylabel("freq")
        ax.label_outer()
        ax.set_xticks(np.arange(1, 10, step=1))
        ax.set_yticks(np.arange(0, .4, step=.05))

    fig.savefig(f"plots/frequency_graphs.png")
    fig.savefig(f"plots/frequency_graphs.pdf")
