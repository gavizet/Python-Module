"""Implementation of a Kmeans algorithm."""
import sys
import argparse
import numpy as np
from Module_02.ex_03.csvreader import CsvReader


class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.

        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.

        Return:
            None.
        """
        pass

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.

        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.

        Return:
            the prediction has a numpy.ndarray, a vector of dimension m * 1.
        """
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-filepath", default="Module_03/ex_04/solar_system.csv", type=str, required=True)
    parser.add_argument("-ncentroid", default=5, type=int, required=True)
    parser.add_argument("-max_iter", default=20, type=int, required=True)
    args = parser.parse_args(sys.argv[1:])
    if args.ncentroid < 1 or args.max_iter < 1:
        print("Error : ncentroid and max_iter have to be positive")
    kmeans = KmeansClustering(ncentroid=args.ncentroid, max_iter=args.max_iter)
    with CsvReader(args.filepath, header=True) as file:
        file_data = np.array(file.getdata())
        print(file_data)
# Usage :
# python Module_03/ex_04/Kmeans.py -filepath="Module_03/ex_04/solar_system_census.csv" -ncentroid=4 -max_iter=3
