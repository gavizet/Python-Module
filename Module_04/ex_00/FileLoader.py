""" The goal of this exercise is to create a Fileloader class containing a load and a display
method."""
import pandas as pd


class Fileloader:

    def __init__(self):
        pass

    def is_valid_file(self, path) -> bool:
        if path is None:
            return False
        if not isinstance(path, str):
            return False
        return True

    def load(self, path):
        if not self.is_valid_file(path):
            return "Not a valid file, try again"
        try:
            events = pd.read_csv(path)
            print(events.shape)
            return events

        except (FileNotFoundError, ValueError):
            print("Not a valid file path, try again")

    def display(self, dataframe, nrows) -> None:
        if not isinstance(nrows, int):
            return "Please input a valid number indicating how many rows you want to display"


if __name__ == "__main__":
    loader = Fileloader()
    data = loader.load("Module_04/ex_00/athlete_events.csv")
    # print(data)
    # loader.display(data, 3)
