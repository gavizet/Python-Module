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
    def euclidian_distance(vector1, vector2):
        # Also called L2 distance because using Minkowski distance with p as 2
        # Could use numpy methods instead but meh, here to learn
        euclidian_distance = sum(abs(v1_i - v2_i) ** 2
                                 for v1_i, v2_i in zip(vector1, vector2)) ** 0.5
        return euclidian_distance

    @staticmethod
    def manhattan_distance(vector1, vector2):
        # Also called L1 distance because using Minkowski distance with p as 1
        # Could use numpy methods instead but meh, here to learn
        manhattan_distance = sum(abs(v1_i - v2_i)
                                 for v1_i, v2_i in zip(vector1, vector2))
        return manhattan_distance

    @staticmethod
    def cosine_distance(vector1, vector2):
        # Could use numpy methods instead but meh, here to learn
        dot, v1_magn, v2_magn = 0, 0, 0
        for v1_num, v2_num in zip(vector1, vector2):
            dot += v1_num * v2_num
            v1_magn += v1_num ** 2
            v2_magn += v2_num ** 2
        cosine_similarity = dot / ((v1_magn ** 0.5) * (v2_magn ** 0.5))
        # Cosine distance is the contrary of cosine similarity, i.e 1 - cosine_similarity
        return float(1 - cosine_similarity)

    @staticmethod
    def manhattan_normalize(vector):
        norm = sum(vector)
        return vector / norm

    @staticmethod
    def euclidian_normalize(vector):
        norm = np.sqrt(sum(vector ** 2))
        return vector / norm


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

    def range_standardize_data(self, X):
        # Get max value for weight, height and bone density columns
        my_max = np.max(X, axis=0)[1:]
        # Get min value for weight, height and bone density columns
        my_min = np.min(X, axis=0)[1:]
        # Doing range standardization => (X - Xmin) / (Xmax - Xmin) for each value
        # Broadcasting to column at index 1, 2, 3 (ommitting 0, i.e index)
        X[:, (1, 2, 3)] = (X[:, (1, 2, 3)] -
                           my_min) / (my_max - my_min)


def parse_args():
    """Parse command line arguments with argparse module

    Raises:
        ValueError: if ncentroid or max_iter arguments are < 1

    Returns:
        args: our argument object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-filepath", default="Module_03/ex_04/solar_system_census.csv", type=str, required=True)
    parser.add_argument("-ncentroid", default=5, type=int, required=True)
    parser.add_argument("-max_iter", default=20, type=int, required=True)
    arguments = parser.parse_args(sys.argv[1:])
    if arguments.ncentroid < 1 or arguments.max_iter < 1:
        raise ValueError("ncentroid and max_iter have to be positive")
    return arguments


if __name__ == "__main__":
    args = parse_args()
    kmeans = KmeansClustering(ncentroid=args.ncentroid, max_iter=args.max_iter)
    npc = NumPyCreator()
    with CsvReader(args.filepath, header=True) as file:
        file_header = np.array(file.getheader())
        # Get all file data as list of floats
        file_data = npc.from_list(file.getdata(), float)
        kmeans.range_standardize_data(file_data)
    # v1 = file_data[-2][1:]
    # v2 = file_data[-1][1:]
    # v3 = np.array([2.0, 0.0, 0.0])
    # print(v1)
    # print(v2)
    # distance = VectorDistance()
    # print("==== V1 & V2 ====")
    # euclidian = distance.euclidian_distance(v1, v2)
    # print(f"Euclidian: {euclidian}")
    # manhattan = distance.manhattan_distance(v1, v2)
    # print(f"Manhattan: {manhattan}")
    # cosine = distance.cosine_distance(v1, v2)
    # print(f"Cosine: {cosine*10}")
    # print("==== V1 & V3 ====")
    # euclidian = distance.euclidian_distance(v1, v3)
    # print(f"Euclidian: {euclidian}")
    # manhattan = distance.manhattan_distance(v1, v3)
    # print(f"Manhattan: {manhattan}")
    # cosine = distance.cosine_distance(v1, v3)
    # print(f"Cosine: {cosine*10}")


# Usage :
# python Module_03/ex_04/Kmeans.py -filepath="Module_03/ex_04/solar_system_census.csv" -ncentroid=4 -max_iter=3
