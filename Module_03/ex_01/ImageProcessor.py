""" Basic manipulation of images via matplotlib library """
import numpy as np
import matplotlib.pyplot as mp_plt
import matplotlib.image as mp_img


class ImageProcessor:
    """ Guess what, it's an image processor """

    def __init__(self):
        pass

    @staticmethod
    def load(path: str):
        """ Loads an image from a given path using matplotlib and prints its dimensions.

        Args:
            path (str): file path of the image that needs to be loaded.

        Returns:
            NumPy array representing an image loaded from the specified path.
        """
        try:
            image_nparray = mp_img.imread(path)
            print(
                f"Loading image of dimensions : {image_nparray.shape[0]}x{image_nparray.shape[1]}")
            return image_nparray
        except Exception as exc:
            print(
                f"Exception: {exc.__class__.__name__} "
                f"at line {exc.__traceback__.tb_lineno} "
                f"of {__file__} -"
                f"{exc}")
            return None

    @staticmethod
    def display(array: np.ndarray):
        """ Displays a numpy array as an image using matplotlib.

        Args:
            array (np.ndarray): the array to be represented
        """
        if not isinstance(array, np.ndarray):
            raise ValueError("Not a numpy array")
        mp_plt.axis("off")
        mp_plt.imshow(array)
        mp_plt.show()


if __name__ == "__main__":
    imp = ImageProcessor()
    # FileNotFoundError
    arr = imp.load("Module_03/ex_01/does_not_exist.png")
    # Empty / Not PNG file
    arr = imp.load("Module_03/ex_01/empty_file.png")
    # Valid PNG input
    arr = imp.load("Module_03/ex_01/42AI.png")
    # Valid nparray
    imp.display(arr)
