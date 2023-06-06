""" The goal of this exercise is to implement a class called SpatioTemporalData that takes
a dataset (pandas.DataFrame) as argument in its constructor and implements two methods. """
import pandas as pd
from Module_04.ex_00.FileLoader import Fileloader


class SpacioTemporalData:
    """ Takes a dataset and implements when and where methods """

    def __init__(self, data: pd.DataFrame):
        if not isinstance(data, pd.DataFrame):
            print("Data argument is not a valid pandas DataFrame")
        self.dataf = data

    def when(self, location) -> list:
        """ Returns a list of the years where Olympic games were held in the given location
        """
        if not isinstance(location, str):
            return "Location should be a string"
        mask = self.dataf['City'].values == location
        result = self.dataf.loc[mask, 'Year'].unique().tolist()
        return result

    def where(self, year) -> list:
        """Returns a list of the locations where the Olympics took place in the given year
        """
        if not isinstance(year, int):
            return "Date should be a valid int"
        mask = self.dataf['Year'].values == year
        result = self.dataf.loc[mask, 'City'].unique().tolist()
        return result


def test_function():
    """ Simple test function"""
    loader = Fileloader()
    data = loader.load("Module_04/ex_00/athlete_events.csv")
    std = SpacioTemporalData(data)

    def test_when_where(function, argument, expected):
        print(f"Result: {function(argument)}")
        print(f"Expected: {expected}")
        print("----------------------")

    test_when_where(std.when, 'London', [2012, 1948, 1908])
    test_when_where(std.when, 'Athina', [2004, 1906, 1896])
    test_when_where(std.when, 'Paris', [1900, 1924])
    test_when_where(std.where, 2000, ['Syndey'])
    test_when_where(std.where, 1980, ['Lake Placid', 'Moskva'])
    test_when_where(std.where, 2016, ["Rio de Janeiro"])


if __name__ == "__main__":
    test_function()
