""" The goal of this exercise is to create a function displaying the proportion of participants
who played a given sport, among the participants of a given genders."""
from Module_04.ex_00.FileLoader import Fileloader


def proportion_by_sport(dataframe, year, sport, sex) -> float:
    """Gets the percentage of participants who played the given sport among the given sex.
        No need to handle input errors, we assume appropriate arguments 

    Args:
        df (pd.DataFrame): pandas dataframe representing the data
        year (int): olympic Year
        sport (str): the given sport
        sex (str): has to be 'M' or 'F'

    Returns:
        float: the percentage of participants
    """
    dataframe = dataframe[(dataframe["Year"].values == year) & (
        dataframe["Sex"].values == sex)]
    len_all = dataframe.shape[0]
    dataframe = dataframe[dataframe['Sport'] == sport]
    len_sport = dataframe.shape[0]
    return len_sport / len_all


def test_function():
    loader = Fileloader()
    data = loader.load("Module_04/ex_00/athlete_events.csv")

    # The rounding of the result does not matter
    # 0.023 or 0.02307969707897584 or 2.3 % are all acceptable
    def test_proportion_by_sport(year, sport, sex, expected):
        print(f"Expected: {expected}")
        print(f"Result: {proportion_by_sport(data, year, sport, sex)}")
        print("----------------------")

    test_proportion_by_sport(2004, 'Tennis', 'F', '0.02307')
    test_proportion_by_sport(2008, 'Hockey', 'F', '0.03284')
    test_proportion_by_sport(1964, 'Biathlon', 'M', '0.00659')


if __name__ == "__main__":
    test_function()
