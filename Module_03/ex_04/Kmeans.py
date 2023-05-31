"""Implementation of a Kmeans algorithm."""
import sys
import argparse
import numpy as np
from Module_02.ex_03.csvreader import CsvReader
from Module_02.ex_05.TinyStatistician import TinyStatistician
from Module_03.ex_00.NumPyCreator import NumPyCreator

# Distance metrics : https://medium.com/@kunal_gohrani/different-types-of-distance-metrics-used-in-machine-learning-e9928c5e26c7
# Python code for distance metrics : https://machinelearningmastery.com/distance-measures-for-machine-learning/
# K-means explanation : https://stanford.edu/~cpiech/cs221/handouts/kmeans.html
# K-means implementation : https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/


class VectorDistance:
    def __init__(self):
        pass

    @staticmethod
    def _euclidian_distance(vector1, vector2):
        # Could use numpy methods instead but meh, here to learn
        euclidian_distance = sum(abs((float(v1_i) - float(v2_i))) ** 2
                                 for v1_i, v2_i in zip(vector1, vector2)) ** 0.5
        return euclidian_distance

    @staticmethod
    def _manhattan_distance(vector1, vector2):
        # Could use numpy methods instead but meh, here to learn
        manhattan_distance = sum(abs((float(v1_i) - float(v2_i)))
                                 for v1_i, v2_i in zip(vector1, vector2))
        return manhattan_distance

    @staticmethod
    def _cosine_distance(vector1, vector2):
        # Could use numpy methods instead but meh, here to learn
        dot, v1_magn, v2_magn = 0, 0, 0
        for v1_num, v2_num in zip(vector1, vector2):
            dot += float(v1_num) * float(v2_num)
            v1_magn += float(v1_num) ** 2
            v2_magn += float(v2_num) ** 2
        cosine_similarity = dot / ((v1_magn ** 0.5) * (v2_magn ** 0.5))
        # Cosine distance is the contrary of cosine similarity, i.e 1 - cosine_similarity
        return float(1 - cosine_similarity)


class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids

    def get_dist(self):
        pass

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
        "-filepath", default="Module_03/ex_04/solar_system_census.csv", type=str, required=True)
    parser.add_argument("-ncentroid", default=5, type=int, required=True)
    parser.add_argument("-max_iter", default=20, type=int, required=True)
    args = parser.parse_args(sys.argv[1:])
    if args.ncentroid < 1 or args.max_iter < 1:
        print("Error : ncentroid and max_iter have to be positive")
    kmeans = KmeansClustering(ncentroid=args.ncentroid, max_iter=args.max_iter)
    npc = NumPyCreator()
    with CsvReader(args.filepath, header=True) as file:
        file_header = np.array(file.getheader())
        file_data = npc.from_list(file.getdata())
        # print(file_data[len(file_data) - 3:])
        # print(file_header)
    v1 = ['186', '186', '94', '0.52']
    v2 = ['187', '193', '95', '0.71']
    distance = VectorDistance()
    euclidian = distance._euclidian_distance(v1[1:], v2[1:])
    print(f"Euclidian: {euclidian}")
    manhattan = distance._manhattan_distance(v1[1:], v2[1:])
    print(f"Manhattan: {manhattan}")
    cosine = distance._cosine_distance(v1[1:], v2[1:])
    print(f"Cosine: {cosine}")


# Usage :
# python Module_03/ex_04/Kmeans.py -filepath="Module_03/ex_04/solar_system_census.csv" -ncentroid=4 -max_iter=3
