import pandas as pd
import graphs
import analysis as an
import fire
import utils


class CovidDataExplorer(object):
    """The various clis for interacting with the covid data"""

    def __init__(self):
        self._data = pd.read_csv("../data/all-states-history.csv")
        self._all_states = self._data["state"].unique()
        self._default_columns = ["positive", "death", "deathIncrease", "positiveCasesViral", "deathConfirmed", "deathProbable"]


    def set_default_columns(self, cols):
        self._default_columns = cols

    def view_default_columns(self):
        """View the default columns used in data analysis"""
        print(self._default_columns)

    def list_columns(self):
        """Lists the columns in the covid data"""
        print(self._data.dtypes)

    def list_states(self):
        """Lists the states in the covid data"""
        for s in self._all_states:
            print(s)

    def graph_usa(self, cols=[], show=True, export=False):
        """Graphs the specified list of columns"""
        if len(cols) == 0:
            cols = self._default_columns
        freq_data = [an.analyse(self._data, col) for col in cols]
        graphs.graph_freq(freq_data, title="Frequency of Digits for US", export=export,  show=show, export_path="USA")

    def graph_state(self, state, cols=[], show=True, export=False):
        """Graph state data for specified or default columns"""
        if len(cols) == 0:
            cols = self._default_columns

        state_data=self._data[self._data["state"] == state]
        state_freq_data = [an.analyse(state_data, col) for col in cols]
        graphs.graph_freq(state_freq_data, title=f"Frequency of Digits for {state}", export=export, show=show,  export_path=state)

    def graph_states(self, states=[], cols=[], show=True, export=False):
        """Graph data for multiple states. Default graphs all, other wise specify states list and cols list"""
        if len(cols) == 0:
            cols = self._default_columns
        if len(states) == 0:
            states = self._all_states
        for state in states:
            self.graph_state(state, cols, show, export)

    def display_usa(self, cols=[]):
        """Display USA data for specified or default columns"""
        if len(cols) == 0:
            cols = self._default_columns
        freq_data = [an.analyse(self._data, col) for col in cols]
        graphs.display_freq(freq_data)

    def display_state(self, state, cols=[]):
        """Display state data for specified or default columns"""
        if len(cols) == 0:
            cols = self._default_columns
        state_data=self._data[self._data["state"] == state]
        state_freq_data = [an.analyse(state_data, col) for col in cols]
        graphs.display_freq(state_freq_data, filter=f"state: {state}")

    def display_states(self, states=[], cols=[]):
        """Display data for all states, or specified states."""
        if len(cols) == 0:
            cols = self._default_columns
        if len(states) == 0:
            states = self._all_states
        for state in states:
            self.display_state(state, cols)


def main():
    cde = CovidDataExplorer()
    commands = {
        'defaultCols': cde.view_default_columns,
        'listCols': cde.list_columns,
        'setDefaultCols': cde.set_default_columns,
        'listStates': cde.list_states,
        'graphUsaCumu': cde.graph_usa,
        'graphState': cde.graph_state,
        'graphStates': cde.graph_states,
        'displayUsaCumu': cde.display_usa,
        'displayState': cde.display_state,
        'displayStates': cde.display_states,
    }
    fire.Fire(commands)

if __name__ == "__main__":
    main()
