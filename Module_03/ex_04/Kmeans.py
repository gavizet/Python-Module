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
        self.max_ = []
        self.min_ = []
        self.dist = VectorDistance()

    def range_standardize_data(self, X):
        # Delete the first column in X, in this case the index
        X = X[:, 1:]
        # Get max value for weight, height and bone density columns
        self.max_ = np.max(X, axis=0)
        # Get min value for weight, height and bone density columns
        self.min_ = np.min(X, axis=0)
        # Broadcasting range standardization to our data
        X = (X - self.min_) / (self.max_ - self.min_)
        return X

    def initialize_centroids(self, X):
        # Update max based on standardized data
        self.max_ = np.max(X, axis=0)
        # Update min based on standardized data
        self.min_ = np.min(X, axis=0)
        # Generate random centroids vectors with data between min and max
        self.centroids = [np.random.uniform(self.min_, self.max_)
                          for i in range(self.ncentroid)]

    def find_closest_cluster(self, distance):
        return np.argmin(distance, axis=1)

    def should_stop(self, iterations, old_centroids):
        if iterations > self.max_iter:
            return True
        return old_centroids == self.centroids

    def label_data(self, data_set):
        distance = np.zeros((data_set.shape[0], self.ncentroid))
        print(distance.shape)

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.

        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.

        Return:
            None.
        """
        X = self.range_standardize_data(X)
        self.initialize_centroids(X)
        print(self.centroids)
        iterations = 0
        old_centroids = None
        while not self.should_stop(iterations, old_centroids):
            iterations += 1
            old_centroids = self.centroids
            self.label_data(X)

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.

        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.

        Return:
            the prediction has a numpy.ndarray, a vector of dimension m * 1.
        """
        pass


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
    with CsvReader(args.filepath, header=True) as file:
        file_header = np.array(file.getheader())
        # Get all file data as list of floats
        file_data = NumPyCreator().from_list(file.getdata(), float)
        kmeans = KmeansClustering(
            ncentroid=args.ncentroid, max_iter=args.max_iter)
        kmeans.fit(file_data)
        kmeans.predict(file_data)


# Usage :
# python Module_03/ex_04/Kmeans.py -filepath="Module_03/ex_04/solar_system_census.csv" -ncentroid=4 -max_iter=3
