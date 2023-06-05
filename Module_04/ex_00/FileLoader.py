""" The goal of this exercise is to create a Fileloader class containing a load and a display
method."""
import pandas as pd


class Fileloader:
    """ Loads and displays a pandas dataframe """

    def __init__(self):
        pass

    @staticmethod
    def load(path):
        """ Loads a CSV file from a path and returns the data as a pandas dataframe,

        Args:
          path (str): represents the file path of the CSV file that needs to be loaded.

        Returns:
          events (pd.DataFrame): contains the data from the CSV file
          None: if an error was found
        """
        events = None
        try:
            events = pd.read_csv(path)
            print(f"Loading dataset of dimensions"
                  f" {events.shape[0]} x {events.shape[1]}")
        except pd.errors.EmptyDataError:
            print("Empty csv file!")
        except (FileNotFoundError, ValueError):
            print("Csv file not found")
        return events

    @staticmethod
    def display(dataframe, nrows) -> None:
        """Dispays the first/last nrows of a pandas dataframe passed as argument

        Args:
            dataframe (pd.DataFrame): a pandas dataframe
            nrows (int): number of rows to display, can be an int of any value
        """
        if not isinstance(nrows, int):
            print("Please enter a valid int")
        elif not isinstance(dataframe, pd.DataFrame):
            print("Not a valid pandas dataframe")
        elif nrows > dataframe.shape[0] or -nrows > dataframe.shape[0]:
            print(f"nrows higher than dataframe of shape : {dataframe.shape}")
        else:
            if nrows < 0:
                print(dataframe.tail(-nrows))
            elif nrows > 0:
                print(dataframe.head(nrows))


def tests():
    """ Some simples tests for FileLoader class """
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
    print("--- Random string not valid test, should output error message ---")
    loader.display(data, "lol")
    print("--- Int higher than filesize test, sould output error message ---")
    loader.display(data, 3000000000)
    print("--- Zero rows valid test, should output nothing ---")
    loader.display(data, 0)
    print("--- Positive int valid test ---")
    loader.display(data, 3)
    print("--- Negative int valid test ---")
    loader.display(data, -3)


if __name__ == "__main__":
    tests()
