""" The goal of this exercise is to implement a function that will return a dictionary
of dictionaries giving the number and type of medals for each year during which the
participant won medals. """
from Module_04.ex_00.FileLoader import Fileloader


# See this article about performance when iterating over panda Dataframes :
# https://towardsdatascience.com/efficiently-iterating-over-rows-in-a-pandas-dataframe-7dd5f9992c01
# And this stackoverflow post
# https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
# TLDR : DO NOT iterate over dataframe rows, it is an anti pattern. Vectorize.

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
    name_mask = dataframe['Name'].values == name
    # Reduce dataframe to only contain the Year and Medal columns
    dataframe = dataframe.loc[name_mask, ['Year', 'Medal']]
    # Returns list with each year our 'name' participated in
    participation_years = dataframe['Year'].unique()
    # Create dict based on the participation_years list
    result = dict.fromkeys(participation_years)
    medals = ['Gold', 'Silver', 'Bronze']
    # Iterate though our list of years
    for year in participation_years:
        result[year] = {'G': 0, 'S': 0, 'B': 0}
        # Fill 'medal' key based on how many the candidate got for that specific year
        for medal in medals:
            medal_mask = (dataframe['Year'] == year) & (
                dataframe['Medal'] == medal)
            result[year][medal[0]] = len(dataframe[medal_mask])
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
