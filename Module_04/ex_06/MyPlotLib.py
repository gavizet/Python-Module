''' The goal the exercise is to introduce plotting methods among the different libraries
Pandas, Matplotlib, Seaborn or Scipy.'''
import matplotlib.pyplot as plt
import pandas as pd
from Module_04.ex_00.FileLoader import Fileloader


class MyPlotLib:
    """Simple plotting class using pandas and matplotlib"""

    def __init__(self):
        pass

    @staticmethod
    def histogram(data, features):
        """ Plots one histogram for each numerical feature in the list.
        """
        num_features = len(features)
        fig, axes = plt.subplots(ncols=num_features)
        for col, ax in zip(features, axes):
            data[col].dropna().plot.hist(ax=ax, title=col, grid=True)
            plt.tight_layout()
        plt.show()

    @staticmethod
    def density(data, features):
        """ Plots the density curve of each numerical feature in the list.
        """
        data[features].dropna().plot.kde()
        plt.show()

    @staticmethod
    def pair_plot(data, features):
        """ Plots a matrix of subplots (also called scatter plot matrix).
        On each subplot shows a scatter plot of one numerical variable against another one
        """
        pd.plotting.scatter_matrix(data[features])
        plt.show()

    @staticmethod
    def box_plot(data, features):
        """ Displays a box plot for each numerical variable in the dataset."""
        data[features].dropna().plot.box()
        plt.show()


def test_function():
    """ Simple test function for MyPlotLib class
    """
    loader = Fileloader()
    data = loader.load("Module_04/ex_00/athlete_events.csv")
    my_plot = MyPlotLib()

    # I completely making a function to pare features, so just assuming we're always
    # passed valid arguments
    def test_myplotlib(features):
        my_plot.histogram(data, features)
        my_plot.density(data, features)
        my_plot.pair_plot(data, features)
        my_plot.box_plot(data, features)

    test_myplotlib(['Weight', 'Height'])
    # test_myplotlib(['Age', 'Weight', 'Height'])
    # test_myplotlib(['Height'])


if __name__ == "__main__":
    test_function()
