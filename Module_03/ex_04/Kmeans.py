"""Implementation of a Kmeans algorithm."""
import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt
from Module_02.ex_03.csvreader import CsvReader
from Module_03.ex_00.NumPyCreator import NumPyCreator

# Distance metrics : https://medium.com/@kunal_gohrani/different-types-of-distance-metrics-used-in-machine-learning-e9928c5e26c7
# Python code for distance metrics : https://machinelearningmastery.com/distance-measures-for-machine-learning/
# K-means explanation : https://stanford.edu/~cpiech/cs221/handouts/kmeans.html
# K-means implementation : https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/


class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids
        self.max_ = []
        self.min_ = []

    def range_standardize_data(self, data_set):
        # Delete the first column in X, in this case the index
        data_set = data_set[:, 1:]
        # Get max value for weight, height and bone density columns
        self.max_ = np.max(data_set, axis=0)
        # Get min value for weight, height and bone density columns
        self.min_ = np.min(data_set, axis=0)
        # Broadcasting range standardization to our data
        data_set = (data_set - self.min_) / (self.max_ - self.min_)
        return data_set

    def initialize_centroids(self, data_set):
        # Update max based on standardized data
        self.max_ = np.max(data_set, axis=0)
        # Update min based on standardized data
        self.min_ = np.min(data_set, axis=0)
        # Generate random centroids vectors with data between min and max
        self.centroids = np.array([np.random.uniform(self.min_, self.max_)
                                   for i in range(self.ncentroid)])

    def should_stop(self, iterations, old_centroids):
        if iterations > self.max_iter:
            return True
        return np.array_equal(old_centroids, self.centroids)

    def find_closest_cluster(self, distance):
        return np.argmin(distance, axis=1)

    def manhattan_distance(self, data_set, centroid):
        return np.sum(np.abs(data_set - centroid), axis=1)

    def euclidian_distance(self, data_set, centroid):
        return np.linalg.norm(data_set - centroid, axis=1)

    def compute_distances(self, data_set, centroids):
        # Create 2D array of size : len_of_data_set x num_of_centroids
        distance = np.zeros((data_set.shape[0], self.ncentroid))
        for k in range(self.ncentroid):
            # Apply pythagore to all rows of data_set compared to centroid[k] and
            # store those values in distance's k column
            distance[:, k] = self.euclidian_distance(data_set, centroids[k, :])
        return distance

    def compute_centroids(self, data_set, labels, old_centroids):
        centroids = np.zeros((self.ncentroid, data_set.shape[1]))
        for k in range(self.ncentroid):
            # Make a 2D array containing all data points (1D array) that have
            # centroid[k] as their closest
            new_labels = data_set[labels == k, :]
            if new_labels.size > 0:
                # If any data point has centroid[k] as their closest,
                # update our centroid[k] value with he mean of all those data points
                centroids[k, :] = np.mean(new_labels, axis=0)
            else:
                # If no data point has centroid[k] as their closest,
                # then reassign to old centroid value so we can keep looping
                centroids[k] = old_centroids[k]
        return centroids

    def fit(self, data_set):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.

        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.

        Return:
            None.
        """
        iterations = 0
        old_centroids = None
        data_set = self.range_standardize_data(data_set)
        self.initialize_centroids(data_set)
        # Loop until we reach max_iter or centroids don't change anymore
        while not self.should_stop(iterations, old_centroids):
            iterations += 1
            old_centroids = self.centroids
            # Returns a 2D array of shape(number_of_data_point, number_of_centroids)
            # containing the distance of each data point compared to each centroid.
            dists = self.compute_distances(data_set, self.centroids)
            # Returns a 1D array containing the index at which the closest centroid can be found for each data point.
            # For example, labels[10] would contain an int representing the n-th centroid that is closest to the 10th data point.
            labels = self.find_closest_cluster(dists)
            self.centroids = self.compute_centroids(
                data_set, labels, old_centroids)
        print(f"Iterations: {iterations}")

    def predict(self, data_set):
        """
        Predict from wich cluster each datapoint belongs to.

        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.

        Return:
            the prediction has a numpy.ndarray, a vector of dimension m * 1.
        """
        # Delete first column (index) and standardize data
        data_set = self.range_standardize_data(data_set)
        # Returns 2D array containing the distance of each data point compared to each centroid.
        dists = self.compute_distances(data_set, self.centroids)
        # Returns a 1D array with each data point containg the number of the closest centroid
        labels = self.find_closest_cluster(dists)
        return labels

    def display_plot(self, data_set, my_labels):
        data_set = self.range_standardize_data(data_set)
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        cluster_labels = my_labels
        cluster_centers = self.centroids
        ax.set_xlabel("Height")
        ax.set_ylabel("Weight")
        ax.set_zlabel("Bone Density")
        colorstr = ["red", "blue", "green", "purple"]
        for k in range(self.ncentroid):
            mask = cluster_labels == k
            center = cluster_centers[k]
            color = colorstr[k] if (k < len(colorstr)) else None
            print(
                f"{sum(mask)} citizens for centroid[{k}] with coords: {center}")
            ax.scatter(data_set[mask, 0], data_set[mask, 1],
                       data_set[mask, 2], color=color)
            ax.scatter(center[0], center[1], center[2], color=color,
                       marker="o", s=200, label="centroids")
        ax.legend
        plt.show()


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
        all_labels = kmeans.predict(file_data)
        kmeans.display_plot(file_data, all_labels)


# Usage :
# python Module_03/ex_04/Kmeans.py -filepath="Module_03/ex_04/solar_system_census.csv" -ncentroid=4 -max_iter=3
