"""Implementation of a Kmeans algorithm."""
import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt
from Module_02.ex_03.csvreader import CsvReader
from Module_03.ex_00.NumPyCreator import NumPyCreator

# Distance metrics : https://medium.com/@kunal_gohrani/different-types-of-distance-metrics-used-in-machine-learning-e9928c5e26c7
# K-means explanation : https://stanford.edu/~cpiech/cs221/handouts/kmeans.html
# K-means plot scattering : https://towardsdatascience.com/k-means-clustering-algorithm-applications-evaluation-methods-and-drawbacks-aa03e644b48a
# Interesting paper about K-means : https://ai.stanford.edu/~acoates/papers/coatesng_nntot2012.pdf
# Another paper, with less depth : https://arxiv.org/ftp/arxiv/papers/1503/1503.00900.pdf


class KmeansClustering:
    """ Runs a basic Kmeans algorithm"""

    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids
        self.max_ = []
        self.min_ = []

    def standardize_data(self, data_set):
        """ Apply min-max standardization to our data"""
        # Delete the first column in X, in this case the index
        data_set = data_set[:, 1:]
        # Get max value for weight, height and bone density columns
        self.max_ = np.max(data_set, axis=0)
        # Get min value for weight, height and bone density columns
        self.min_ = np.min(data_set, axis=0)
        # Broadcasting min-max standardization to our data
        data_set = (data_set - self.min_) / (self.max_ - self.min_)
        return data_set

    def initialize_centroids(self, data_set):
        """ Initialize centroids with random data between the min and max of our data set."""
        # Update max based on standardized data
        self.max_ = np.max(data_set, axis=0)
        # Update min based on standardized data
        self.min_ = np.min(data_set, axis=0)
        # Generate random centroids vectors with data between min and max
        self.centroids = np.array([np.random.uniform(self.min_, self.max_)
                                   for i in range(self.ncentroid)])

    def should_stop(self, iterations, old_centroids):
        """ Returns True if we've hit max_iter or if centroids did not change, False otherwise"""
        if iterations > self.max_iter:
            return True
        return np.array_equal(old_centroids, self.centroids)

    def find_closest_cluster(self, distance):
        """ Returns the index of the closest centroid in the distance array"""
        return np.argmin(distance, axis=1)

    def euclidian_distance(self, data_set, centroid):
        """ Returns the normalized euclidian distance between each data point in 
        our data_set and the centroid
        """
        return np.linalg.norm(data_set - centroid, axis=1)

    def get_distances(self, data_set, centroids):
        """Computes the normalized euclidian distance between each data point and each centroid.
        Stores the result in a 2D distance array of shape (len of data set * num of centroids)

        Args:
            centroids (ndarray): numpy array containing our centroids data

        Returns:
            distance (numpy.ndarray): 2D dimension m * ncentroid containing
                the distance between each data point and each centroid.
        """
        # Create 2D array of size : len_of_data_set x num_of_centroids
        distance = np.zeros((data_set.shape[0], self.ncentroid))
        for k in range(self.ncentroid):
            # Apply euclidian normalization to all rows of data_set compared to centroid[k]
            # and store those values in distance's k column
            distance[:, k] = self.euclidian_distance(data_set, centroids[k, :])
        return distance

    def get_centroids(self, data_set, labels, old_centroids):
        """ Update our centroid ndarray based on the mean of all data points that
            have the specific centroid as their closest.

        Args:
            labels (ndarray): 1D numpy array containing the closest centroid for each data point
            old_centroids (ndarray): copy of self.centroids

        Returns:
            centroids (numoy.ndarray): 2D numpy array containing our updated centroids
        """
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

    def fit(self, data_set) -> None:
        """
        Run the K-means clustering algorithm.

        For the location of the initial centroids, random pick ncentroids from the dataset.
        Loop of 3 steps until when we hit max_iter or centroids don't change anymore:
            => For each data point, store the closest centroid in terms of euclidian distance
            => Update our centroids based on the mean of all data points that have the
                specific centroid as their closest.

        Args:
            data_set (numpy.ndarray): matrice of dimension m * n.
        """
        iterations = 0
        old_centroids = None
        # Min-max standardization of data so weight, height and bone_density
        # have the same importance
        data_set = self.standardize_data(data_set)
        self.initialize_centroids(data_set)
        # Loop until we reach max_iter or centroids don't change anymore
        while not self.should_stop(iterations, old_centroids):
            iterations += 1
            old_centroids = self.centroids
            # Returns a 2D array of shape(number_of_data_point, number_of_centroids)
            # containing the distance of each data point compared to each centroid.
            dists = self.get_distances(data_set, self.centroids)
            # Returns a 1D array containing the index at which the closest centroid
            # can be found for each data point.
            # For example, labels[10] would contain an int representing the n-th
            # centroid that is closest to the 10th data point.
            labels = self.find_closest_cluster(dists)
            # Update our centroid array based on the labels
            self.centroids = self.get_centroids(data_set, labels,
                                                old_centroids)
        print(f"Iterations: {iterations}")

    def predict(self, data_set):
        """ Predict from wich cluster each datapoint belongs to.

        Args:
            data_set (numpy.ndarray): a matrice of dimension m * n.

        Return:
            labels (numpy.ndarray): m * 1.
            Contains the index of the closest centroid for each data point.
        """
        # Min-max standardization of data so weight, height and bone_density
        # have the same importance
        data_set = self.standardize_data(data_set)
        # Returns 2D array containing the distance of each data point compared to each centroid.
        dists = self.get_distances(data_set, self.centroids)
        # Returns a 1D array with each data point containg the number of the closest centroid
        labels = self.find_closest_cluster(dists)
        return labels

    def display_plot(self, data_set, cluster_labels):
        """Display the plot in 3D using matplotlib.pyplot

        Args:
            data_set (numpy.ndarray): 2D, a matrice of dimension m * n.
            cluster_labels (numpy.ndarray): 1D, dimension m * 1
        """
        data_set = self.standardize_data(data_set)
        figure = plt.figure(figsize=(8, 8))
        axes = plt.axes(projection='3d')
        centroids = self.centroids
        axes.set_xlabel("Height", fontweight='bold')
        axes.set_ylabel("Weight", fontweight='bold')
        axes.set_zlabel("Bone Density", fontweight='bold')
        plt.title(f"Kmeans with {self.ncentroid} centroids "
                  f"and {len(data_set)} data points",
                  fontweight='bold')
        colorstr = ["red", "blue", "green", "brown"]
        for k in range(self.ncentroid):
            mask = (cluster_labels == k)
            color = colorstr[k] if (k < len(colorstr)) else None
            print(
                f"{sum(mask)} citizens for centroid[{k}] with coords: {centroids[k]}")
            weight = data_set[mask, 0]
            height = data_set[mask, 1]
            bone_density = data_set[mask, 2]
            axes.scatter(weight, height,
                         bone_density, color=color)
            axes.scatter(centroids[k][0], centroids[k][1], centroids[k][2],
                         color=color, s=200, label="Centroids")
        plt.show()


def parse_args():
    """Parse command line arguments with argparse module

    Raises:
        ValueError: if ncentroid or max_iter arguments are < 1

    Returns:
        args: our argument object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-filepath", default="Module_03/ex_04/solar_system_census.csv",
                        type=str, required=True)
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
        kmeans = KmeansClustering(ncentroid=args.ncentroid,
                                  max_iter=args.max_iter)
        kmeans.fit(file_data)
        data_labels = kmeans.predict(file_data)
        kmeans.display_plot(file_data, data_labels)

# Usage :
# python Module_03/ex_04/Kmeans.py -filepath="Module_03/ex_04/solar_system_census.csv" -ncentroid=4 -max_iter=3
