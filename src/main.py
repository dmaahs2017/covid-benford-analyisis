import pandas as pd
import graphs
import analysis as an
import fire

data = pd.read_csv("../data/all-states-history.csv")
all_states = data["state"].unique()
default_columns = ["positive", "death", "deathIncrease", "positiveCasesViral", "deathConfirmed", "deathProbable"]

class CovidDataExplorer(object):
    """The various clis for interacting with the covid data"""

    def view_default_columns(self):
        """View the default columns used in data analysis"""
        print(default_columns)

    def list_columns(self):
        """Lists the columns in the covid data"""
        print(data.dtypes)

    def list_states(self):
        """Lists the states in the covid data"""
        for s in all_states:
            print(s)

    def graph_usa(self, cols=default_columns, show=True, export=False):
        """Graphs the specified list of columns"""
        freq_data = [an.analyse(data, col) for col in cols]
        graphs.graph_freq(freq_data, title="Frequency of Digits for US", export=export,  show=show, export_path="USA")

    def graph_state(self, state, cols=default_columns, show=True, export=False):
        """Graph state data for specified or default columns"""
        state_data=data[data["state"] == state]
        state_freq_data = [an.analyse(state_data, col) for col in cols]
        graphs.graph_freq(state_freq_data, title=f"Frequency of Digits for {state}", export=export, show=show,  export_path=state)

    def graph_states(self, states=all_states, cols=default_columns, show=False, export=True):
        """Graph data for multiple states. Default graphs all, other wise specify states list and cols list"""
        for state in states:
            self.graph_state(state, cols, show, export)

    def display_usa(self, cols=default_columns):
        """Display USA data for specified or default columns"""
        freq_data = [an.analyse(data, col) for col in cols]
        graphs.display_freq(freq_data)

    def display_state(self, state, cols=default_columns):
        """Display state data for specified or default columns"""
        state_data=data[data["state"] == state]
        state_freq_data = [an.analyse(state_data, col) for col in cols]
        graphs.display_freq(state_freq_data, filter=f"state: {state}")

    def display_states(self, states=all_states, cols=default_columns):
        """Display data for all states, or specified states."""
        for state in states:
            self.display_state(state, cols)


def main():
    fire.Fire(CovidDataExplorer(), name='cde')

if __name__ == "__main__":
    main()
