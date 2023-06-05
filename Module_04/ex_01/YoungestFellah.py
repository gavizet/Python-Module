import pandas as pd
from Module_04.ex_00.FileLoader import Fileloader


def youngest_fellah(dataframe: pd.DataFrame, year: int):
    pass


def tests():
    """ Some simples tests for FileLoader class """
    loader = Fileloader()
    data = loader.load("Module_04/ex_00/athlete_events.csv")

    youngest_fellah(data, 2004)


if __name__ == "__main__":
    tests()
