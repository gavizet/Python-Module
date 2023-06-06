""" The goal of this exercise is to implement a class called SpatioTemporalData that takes
a dataset (pandas.DataFrame) as argument in its constructor and implements two methods. """
import pandas as pd
from Module_04.ex_00.FileLoader import Fileloader


class SpacioTemporalData:

    def __init__(self, data=None):
        if not isinstance(data, pd.DataFrame):
            print("Data argument is not a valid pandas DataFrame")
        self.data = data

    def when(self, location):
        mask = ()
        pass

    def where(self, date):
        pass


def test_function():
    loader = Fileloader()
    data = loader.load("Module_04/ex_00/athlete_events.csv")
    std = SpacioTemporalData(data)

    def test_when_where(function, argument, expected):
        print(f"Result: {function(argument)}")
        print(f"Expected: {expected}")
        print("----------------------")

    test_when_where(std.when, 'London', [2012, 1948, 1908])
    test_when_where(std.when, 'Athina', [2004, 1906, 1896])
    test_when_where(std.when, 'Athina', [1900, 1924])
    test_when_where(std.where, '2000', ['Syndey'])
    test_when_where(std.where, '1980', ['Lake Placid', 'Moskva'])
    test_when_where(std.where, '2016', ["Rio de Janeiro"])


if __name__ == "__main__":
    test_function()
