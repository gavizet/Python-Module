"""Discovering some panda methods"""
import pandas as pd
from Module_04.ex_00.FileLoader import Fileloader


def youngest_fellah(dataframe: pd.DataFrame, year: int):
    """ Finds the youngest man & woman who took parts in the Olympics for a given year

    Args:
        dataframe (pd.DataFrame): a pandas dataframe containing Olympics data
        year (int): year we want to get the youngest f & m for

    Returns:
        dict: contains 2 keys with the youngest male & female athlete for a given year
    """
    if not isinstance(dataframe, pd.DataFrame):
        return "Not a valid pandas dataframe"
    if not isinstance(year, int):
        return "Year has to be an int"
    result = {'f': float("nan"), 'm': float("nan")}
    youngest_man = dataframe.loc[(dataframe["Year"] == year)
                                 & (dataframe["Sex"] == 'M'), "Age"]
    youngest_woman = dataframe.loc[(dataframe["Year"] == year)
                                   & (dataframe["Sex"] == 'F'), "Age"]
    result['m'] = youngest_man.min()
    result['f'] = youngest_woman.min()
    return result


def tests():
    """ Some simples tests for FileLoader class """
    loader = Fileloader()
    data = loader.load("Module_04/ex_00/athlete_events.csv")

    print(youngest_fellah(data, "test"))
    # output is: an error message

    print(youngest_fellah("test", 2002))
    # output is: an error message

    print(youngest_fellah(data, 1992))
    # output is: "{'f': 12.0, 'm': 11.0}"

    print(youngest_fellah(data, 2004))
    # output is: "{'f': 13.0, 'm': 14.0}"

    print(youngest_fellah(data, 2010))
    # output is: "{'f': 15.0, 'm': 15.0}"

    print(youngest_fellah(data, 2003))
    # output is: "{'f': nan, 'm': nan}"


if __name__ == "__main__":
    tests()
