"""Discovering some panda methods"""
import pandas as pd
from Module_04.ex_00.FileLoader import Fileloader

# See this stackoverflow page for indexing performance with pandas :
# https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values


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
    man_mask = (dataframe["Year"].values == year) & \
        (dataframe["Sex"].values == 'M')
    female_mask = (dataframe["Year"].values == year) & \
        (dataframe["Sex"].values == 'F')
    youngest_man = dataframe.loc[man_mask, "Age"]
    youngest_woman = dataframe.loc[female_mask, "Age"]
    result['m'] = youngest_man.min()
    result['f'] = youngest_woman.min()
    return result


def tests():
    """ Some simples tests for FileLoader class """
    loader = Fileloader()
    data = loader.load("Module_04/ex_00/athlete_events.csv")

    print(youngest_fellah(data, "test"))
    # expected output is: an error message

    print(youngest_fellah("test", 2002))
    # expected output is: an error message

    print(youngest_fellah(data, 2003))
    # expected output is: "{'f': nan, 'm': nan}"

    print(youngest_fellah(data, 1992))
    # expected output is: "{'f': 12.0, 'm': 11.0}"

    print(youngest_fellah(data, 2004))
    # expected output is: "{'f': 13.0, 'm': 14.0}"

    print(youngest_fellah(data, 2010))
    # expected output is: "{'f': 15.0, 'm': 15.0}"


if __name__ == "__main__":
    tests()
