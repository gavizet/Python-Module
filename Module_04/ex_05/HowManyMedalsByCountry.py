""" The goal of this exercise is to write a function that returns a dictionary of
dictionaries giving the number and type of medal for each competition where the
country delegation earned medals """
import pandas as pd
from Module_04.ex_00.FileLoader import Fileloader


# Stackoverflow on how to get rows based on column data :
# https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values

team_sports = [
    'Basketball',
    'Football',
    'Tug-Of-War',
    'Badminton',
    'Sailing',
    'Handball',
    'Water Polo',
    'Hockey',
    'Rowing',
    'Bobsleigh',
    'Softball',
    'Volleyball',
    'Synchronized Swimming',
    'Baseball',
    'Rugby Sevens',
    'Rugby',
    'Lacrosse',
    'Polo'
]


def how_many_medals_by_country(df, country_name) -> dict:
    """ Gets the number and type of medal for each year where the country delegation earned medals

    Args:
        df (pd.Dataframe): the pandas dataframe
        country_name (str): name of the delegation

    Returns:
        dict: nested dict of Olympic years containing keys 'G', 'S' and 'B' for each type of 
        medal won. The innermost values correspond to the number of medals of a given type 
        won for a given year for the specific delegation.
    """
    if not isinstance(df, pd.DataFrame) or not isinstance(country_name, str):
        return {}
    mask = df['Team'].values == country_name
    # Get all rows with containing our 'country_name' argument in 'Team' column
    df = df.loc[mask, ['Year', 'Team', 'Sport', 'Medal']]
    # Get a sorted list with no duplicates of all years where our delegation participated
    medal_years = df['Year'].drop_duplicates().sort_values().tolist()
    # Create dict with keys based on our medal_years list
    result = dict.fromkeys(medal_years)
    # Get all rows which have a team_sport in the 'Sport' column and remove duplicates
    team_sports_rows = df[df['Sport'].isin(team_sports)].drop_duplicates()
    # Get all rows which a solo sport (not in team_sport) in the 'Sport' column
    solo_sports_rows = df[~df['Sport'].isin(team_sports)]
    # Concat the two DataFrames using pandas concat() method
    df = pd.concat([team_sports_rows, solo_sports_rows])
    medals = ['Gold', 'Silver', 'Bronze']
    # Iterate through every Olympic year where our team participated
    for year in medal_years:
        result[year] = {'G': 0, 'S': 0, 'B': 0}
        # Iterate through all the medals
        for medal in medals:
            # Count how many our team got of the specific medal in the specific year,
            # put that value in the dictionary at the appropriate place
            medal_mask = (df['Year'].values == year) & (
                df['Medal'].values == medal)
            result[year][medal[0]] = len(df[medal_mask])
    return result


def test_function():
    """ Simple test function"""
    loader = Fileloader()
    data = loader.load("Module_04/ex_00/athlete_events.csv")

    def test_how_many_medals(name):
        result = how_many_medals_by_country(data, name)
        print(f"Result: {result}")
        print("----------------------")
        print("No comparaison to expected because dataset changed", end=" ")
        print("between correction subject and now.")

    test_how_many_medals('France')
    test_how_many_medals('United States')


if __name__ == "__main__":
    test_function()
