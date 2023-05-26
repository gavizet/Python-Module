""" Manipulation and initiation to slicing method on numpy arrays """
import numpy as np


class ScrapBooker:

    def __init__(self):
        pass

    @staticmethod
    def _is_ndarray(array) -> bool:
        if not isinstance(array, np.ndarray):
            return False
        return True

    @staticmethod
    def _is_valid_dim(dimension) -> bool:
        if not isinstance(dimension, tuple):
            return False
        if len(dimension) != 2:
            return False
        for num in dimension:
            if not isinstance(num, int) or num < 0:
                return False
        return True

    @staticmethod
    def _is_valid_n_axis(array, n, axis) -> bool:
        if not isinstance(axis, int) or not 0 <= axis <= 1:
            return False
        desired_len = len(array) if axis == 1 else len(array[0])
        if n > desired_len:
            return False
        return True

    def crop(self, array, dim, position=(0, 0)):
        """ Crops the image as a rectangle via dim arguments (being the new height and width of the image) from the coordinates given by position arguments.

        Args:
            array: numpy.ndarray
            dim: tuple of 2 integers.
            position: tuple of 2 integers.
        Return:
            new_arr: the cropped numpy.ndarray.
            None (if combinaison of parameters not compatible).
        Raise:
            This function should not raise any Exception.
        """
        if not self._is_ndarray(array)\
            or not self._is_valid_dim(dim)\
                or not self._is_valid_dim(position):
            return None
        x_len = len(array)
        y_len = len(array[0])
        pos_x = position[0]
        pos_y = position[1]
        if pos_x > x_len or pos_y > y_len:
            return None
        dim_x = (pos_x + dim[0]) if pos_x + dim[0] <= x_len else x_len
        dim_y = (pos_y + dim[1]) if pos_y + dim[1] <= y_len else y_len
        return array[pos_x:dim_x, pos_y:dim_y]

    def thin(self, array, n, axis):
        """ Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)

        Args:
            array: numpy.ndarray.
            n: non null positive integer lower than the number of row/column of the array
            axis: positive non null integer.
        Return:
            new_arr: thined numpy.ndarray.
            None (if combinaison of parameters not compatible).
        """
        if not self._is_ndarray(array) or not self._is_valid_n_axis(array, n, axis):
            return None
        # Swap axis so we delete from the right axis
        axis = 0 if axis == 1 else 1
        # Stock all row/column index to delete
        n_to_delete = list(range(n-1, array.shape[axis], n))
        return np.delete(array, n_to_delete, axis)

    def juxtapose(self, array, n, axis):
        """ Juxtaposes n copies of the image along the specified axis.
        Args:
            array: numpy.ndarray.
            n: positive non null integer.
            axis: integer of value 0 or 1.
        Return:
            new_arr: juxtaposed numpy.ndarray.
            None (combinaison of parameters not compatible).
        """
        if not self._is_ndarray(array) or not self._is_valid_n_axis(array, 0, axis):
            return None
        if not isinstance(n, int) or n < 0:
            return None
        array_copy = np.copy(array)
        for index in range(n - 1):
            array = np.concatenate((array, array_copy), axis=axis)
        return array

    def mosaic(self, array, dim):
        return True


if __name__ == "__main__":
    spb = ScrapBooker()
    arr1 = np.arange(0, 25).reshape(5, 5)
    arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
    arr3 = np.array([[var] * 10 for var in "ABCDEFG"])
    arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print("Expect: array([[ 5],\n[10],\n[15]])")
    crop = spb.crop(arr1, (3, 1), (1, 0))
    print(f"Result: {repr(crop)}")
    print("------------------------------")

    print("Expect: array([['A', 'B', 'D', 'E', 'G', 'H'],\n\
      ['A', 'B', 'D', 'E', 'G', 'H'],\n\
      ['A', 'B', 'D', 'E', 'G', 'H'],\n\
      ['A', 'B', 'D', 'E', 'G', 'H'],\n\
      ['A', 'B', 'D', 'E', 'G', 'H'],\n\
      ['A', 'B', 'D', 'E', 'G', 'H']], dtype='<U1')")
    thin1 = spb.thin(arr2, 3, 0)
    print(f"Result: {repr(thin1)}")
    print("------------------------------")

    print("Expect: array([['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],\n\
      ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],\n\
      ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],\n\
      ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],\n\
      ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']], dtype='<U1')")
    thin2 = spb.thin(arr3, 3, 1)
    print(f"Result: {repr(thin2)}")
    print("------------------------------")

    print("Expect: array([[1, 2, 3],\n\
      [4, 5, 6],\n\
      [7, 8, 9],\n\
      [1, 2, 3],\n\
      [4, 5, 6],\n\
      [7, 8, 9]])")
    juxtapose = spb.juxtapose(arr4, 2, 0)
    print(f"Result: {repr(juxtapose)}")
    print("------------------------------")

    """ ERROR TESTS, SHOULD ALL RETURN NONE """
    # Not a numpy array
    assert spb.crop([[1, 2, 3], [4, 5, 6], [7, 8, 9]], (1, 2)) is None
    # Crop exceeding size of array
    assert spb.crop(arr1, (3, 3), (8, 8)) is None
    # Axis not 0 or 1
    assert spb.thin(arr3, 3, 2) is None
    # Negative n
    assert spb.juxtapose(arr4, -2, 0) is None
    # More than 2 int for dimension
    # assert spb.mosaic(arr4, (1, 2, 3)) is None
    print("Error tests passed")
