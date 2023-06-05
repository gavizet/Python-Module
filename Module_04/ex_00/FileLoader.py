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
            print(f"Loading dataset of dimensions"
                  f" {events.shape[0]} x {events.shape[1]}")
            return events
        except pd.errors.EmptyDataError:
            print("Empty csv file!")
        except (FileNotFoundError, ValueError):
            print("Csv file not found")

    def display(self, dataframe, nrows) -> None:
        if not isinstance(nrows, int):
            return "Please input a valid number indicating how many rows you want to display"
        if nrows < 0 and nrows > -dataframe.shape[0]:
            print(dataframe.tail(-nrows))
        elif nrows > 0 and nrows < dataframe.shape[0]:
            print(dataframe.head(nrows))


if __name__ == "__main__":
    loader = Fileloader()
    print("==== TEST LOADER ====")
    print("--- Does not exist test ---")
    data = loader.load("does_not_exist.csv")
    print("--- Random string test ---")
    data = loader.load("lol")
    print("--- Empty file test ---")
    data = loader.load("Module_04/ex_00/empty_file.csv")
    print("--- Valid CSV test ---")
    data = loader.load("Module_04/ex_00/athlete_events.csv")
    print()

    print("==== TEST DISPLAY ====")
    print("--- Random string not valid test, should output nothing ---")
    loader.display(data, "lol")
    print("--- Int higher than filesize test, sould output nothing ---")
    loader.display(data, 3000000000)
    print("--- Zero rows valid test, should output nothing ---")
    loader.display(data, 0)
    print("--- Positive int valid test ---")
    loader.display(data, 3)
    print("--- Negative int valid test ---")
    loader.display(data, -3)
