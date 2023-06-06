""" The goal of this exercise is to implement a function that will return a dictionary
of dictionaries giving the number and type of medals for each year during which the
participant won medals. """
from Module_04.ex_00.FileLoader import Fileloader


def how_many_medals(dataframe, name) -> dict:
    """Gets  the number and type of medals for each year during which the participant won medals.

    Args:
        dataframe (pd.DataFrame): the pandas dataframe
        name (str): the name of the participant

    Returns:
        dict: dict of Olympic years containing sub-dicts 'G', 'S' and 'B' for each type of 
        medal won. The innermost values correspond to the number of medals of a given type 
        won for a given year.
    """
    mask = dataframe['Name'].values == name
    dataframe = dataframe.loc[mask, ['Year', 'Medal']]
    result = {}
    for index, row in dataframe.iterrows():
        if row['Year'] not in result:
            result[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
        if row['Medal'] == 'Gold':
            result[row['Year']]['G'] += 1
        elif row['Medal'] == 'Silver':
            result[row['Year']]['S'] += 1
        elif row['Medal'] == 'Bronze':
            result[row['Year']]['B'] += 1
        else:
            pass
    return result


def test_function():
    loader = Fileloader()
    data = loader.load("Module_04/ex_00/athlete_events.csv")

    def test_how_many_medals(name, expected):
        print(f"Result: {how_many_medals(data, name)}")
        print(f"Expected: {expected}")
        print("----------------------")

    test_how_many_medals(
        'Gary Abraham', "{1976: {'G': 0, 'S': 0, 'B': 0}, 1980: {'G': 0, 'S': 0, 'B': 1}}")
    test_how_many_medals('Yekaterina Konstantinovna Abramova',
                         "{2006: {'G': 0, 'S': 0, 'B': 1}, 2010: {'G': 0, 'S': 0, 'B': 0}}")
    test_how_many_medals('Kristin Otto', "{1988: {'G': 6, 'S': 0, 'B': 0}}")


if __name__ == "__main__":
    test_function()
