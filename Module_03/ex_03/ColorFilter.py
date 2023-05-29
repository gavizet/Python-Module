""" Manipulation of loaded image via numpy arrays, broadcasting. """
import numpy as np
from Module_03.ex_01.ImageProcessor import ImageProcessor

# Useful docs :
# https://yashaslokesh.github.io/inverting-the-colors-of-an-image.html
# https://note.nkmk.me/en/python-numpy-image-processing/
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html
# Matplotlib returns array of floats(0, 1) for PNG, int(0,255) for the rest
# Only PNG (RGBA) will have a 4th channel. 3 fo RBG, 2 for greyscale


class ColorFilter():
    """Class to apply a color filter to an image"""

    def __init__(self):
        pass

    @staticmethod
    def invert(array):
        '''Inverts the color of the image received as a numpy array.

        Args:
            array: numpy.ndarray corresponding to the image.

        Return:
            array: numpy.ndarray corresponding to the transformed image.
        '''
        is_png = array.shape[2] == 4
        if is_png:
            new_array = 1 - array
            # Since we're working with a PNG, we have to take the 4th channel
            # (Alpha, or transparency) into account and transfer it.
            # red would be [:, :, 0], green [:, :, 1], blue [:, : 2]
            new_array[:, :, 3] = array[:, :, 3]
        else:
            new_array = 255 - array
        return new_array

    @staticmethod
    def to_blue(array):
        '''Applies a blue filter to the image received as a numpy array.

        Args:
            array: numpy.ndarray corresponding to the image.

        Return:
            array: numpy.ndarray corresponding to the transformed image.
        '''
        new_array = np.copy(array)
        new_array[:, :, (0, 1)] = 0
        return new_array

    @staticmethod
    def to_green(array):
        '''Applies a green filter to the image received as a numpy array.

        Args:
            array: numpy.ndarray corresponding to the image.

        Return:
            array: numpy.ndarray corresponding to the transformed image.
        '''
        new_array = np.copy(array)
        new_array[:, :, (0, 2)] = 0
        return new_array

    @staticmethod
    def to_red(array):
        '''Applies a red filter to the image received as a numpy array.

        Args:
            array: numpy.ndarray corresponding to the image.

        Return:
            array: numpy.ndarray corresponding to the transformed image.
        '''
        new_array = np.copy(array)
        new_array[:, :, (1, 2)] = 0
        return new_array

    @staticmethod
    def to_celluloid(array):
        '''Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.

        Args:
            array: numpy.ndarray corresponding to the image.

        Return:
            array: numpy.ndarray corresponding to the transformed image.
        '''
        new_array = np.copy(array)
        treshholds = np.linspace(
            array.min(), array.max(), num=4, endpoint=False)
        for shade in treshholds:
            new_array[array > shade] = shade
        return new_array

    @staticmethod
    def to_grayscale(array, filter, **kwargs):
        '''Applies a grayscale filter to the image received as a numpy array.

        Args:
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in [m, mean, w, weight]
            weights: [kwargs] list of 3 floats where the sum equals to 1,
                        corresponding to the weights of each RBG channels.

        Return:
            array: numpy.ndarray corresponding to the transformed image.
        '''
        if filter not in ['m', 'mean', 'w', 'weight']:
            return None
        gray_image = np.copy(array)
        red = array[:, :, 0]
        green = array[:, :, 1]
        blue = array[:, :, 2]
        if filter in ['m', 'mean']:
            weighted = (red + green + blue) / 3
        if filter in ['w', 'weight']:
            red_w, green_w, blue_w = kwargs.get('weights')
            weighted = (red * red_w) + (green * green_w) + (blue * blue_w)
        for color in range(3):
            gray_image[:, :, color] = weighted
        return gray_image


if __name__ == "__main__":
    imgp = ImageProcessor()
    arr = imgp.load('Module_03/ex_03/elon_canaGAN.png')
    cf = ColorFilter()

    f = [
        cf.invert,
        cf.to_blue,
        cf.to_green,
        cf.to_red,
        cf.to_celluloid,
    ]
    for function in f:
        res = function(arr)
        imgp.display(res)

    res = cf.to_grayscale(arr, "m")
    imgp.display(res)
    res = cf.to_grayscale(arr, "w", weights=[0, 0, 1])
    imgp.display(res)
