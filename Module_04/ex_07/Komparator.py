""" The goal the exercise is to introduce plotting methods among the different
libraries Pandas, Matplotlib, Seaborn or Scipy."""
import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import is_numeric_dtype, is_string_dtype
from Module_04.ex_00.FileLoader import Fileloader

# See this stackoverflow on why pandas "string" column have dtype: 'object' :
# https://stackoverflow.com/questions/21018654/strings-in-a-dataframe-but-dtype-is-object
# TLDR : it's in fact a numpy.ndarray object because str is of variable length

# See this stackoverflow for the best way to check dtype of a pandas column :
# https://stackoverflow.com/questions/22697773/how-to-check-the-dtype-of-a-column-in-python-pandas

# See this page about Python decorators :
# https://www.geeksforgeeks.org/python-decorators-a-complete-guide/


class Komparator:
    """ I think it's to compare, not sure though"""

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def _check_args(function):
        def wrapper(self, categorical_var: str, numerical_var: str):
            """ Wrapper function for our _check_args decorator """
            if not isinstance(self.df, pd.DataFrame):
                return None
            if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
                return None
            features_list = self.df.columns.tolist()
            if categorical_var not in features_list or numerical_var not in features_list:
                return None
            if not is_string_dtype(self.df[categorical_var]):
                return None
            if not is_numeric_dtype(self.df[numerical_var]):
                return None
            result = function(self, categorical_var, numerical_var)
            return result
        return wrapper

    @_check_args
    def compare_box_plots(self, categorical_var: str, numerical_var: str):
        """ Displays a series of box plots to compare how the distribution of the numerical 
        variable changes if we only consider the subpopulation which belongs to each category"""
        # Get dataframe with 2 columns of our vars without rows with NaN values
        data = self.df[[categorical_var, numerical_var]].dropna()
        # Pivot the data so that each column is now equal to a unique feature and contains the
        # numerical_var values. I.E, with Sex as categorical_var, columns are now 'M' and 'F'.
        data_pivot = data.pivot(columns=categorical_var, values=numerical_var)
        # Create subplot for each feature (column)
        fig, axes = plt.subplots(ncols=len(data_pivot.columns))
        # Make a box plot for each column of data_pivot
        for col, ax in zip(data_pivot.columns, axes):
            data_pivot[col].plot.box(ax=ax, title=numerical_var)
        plt.show()

    @_check_args
    def density(self, categorical_var: str, numerical_var: str):
        """ Displays a density plot of the numerical variable.
        Each subpopulation is represented by a separate curve on the graph"""
        # Get dataframe with 2 columns of our vars without rows with NaN values
        data = self.df[[categorical_var, numerical_var]].dropna()
        # Pivot the data so that each column is now equal to a unique feature and contains the
        # numerical_var values. I.E, with Sex as categorical_var, columns are now 'M' and 'F'.
        data_pivot = data.pivot(columns=categorical_var,
                                values=numerical_var)
        # Make 1 density plot, with each subpopulation (now our columns) represented
        # by a separate curve on the graph
        data_pivot.plot.kde(legend=True, linewidth=2,
                            title=numerical_var, label=categorical_var)
        plt.show()

    @_check_args
    def compare_histograms(self, categorical_var: str, numerical_var: str):
        """ Display a series of histogram plots of the numerical variable for each category"""
        data = self.df[[categorical_var, numerical_var]].dropna()
        data_pivot = data.pivot(columns=categorical_var, values=numerical_var)
        fig, axes = plt.subplots(ncols=len(data_pivot.columns))
        for col, ax in zip(data_pivot.columns, axes):
            data_pivot[col].plot.hist(ax=ax, title=f"{col} {numerical_var}",
                                      grid=True, bins=20, legend=True)
            plt.tight_layout()
        plt.show()


def test_function():
    """ Simple test function for Komparator class
    """
    loader = Fileloader()
    data = loader.load("Module_04/ex_00/athlete_events.csv")
    komp = Komparator(data)

    def test_komparator(category, number):
        komp.compare_box_plots(category, number)
        komp.density(category, number)
        komp.compare_histograms(category, number)

    # Valid test, should display plot for each method
    test_komparator("Sex", "Height")
    # 2nd arg not a numeric_var, do nothing
    test_komparator("Sex", "Medal")
    # 1st arg not category_var, do nothing
    test_komparator("Weight", "Height")
    # 1st arg not a column in our dataframe, do nothing
    test_komparator("test", "Height")


if __name__ == "__main__":
    test_function()
