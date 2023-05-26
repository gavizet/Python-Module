""" Introduction to numpy library"""
import numpy as np


# The NumPyCreator class is a Python class that has not been defined yet.
class NumPyCreator:
    """ Numpy class"""

    def _check_type(self, data, dtype) -> bool:
        """ Make sure the given nested data is valid

        Args:
            data (list / tuple): data we want to check
            dtype (type): specifies which type we're checking for

        Returns:
            bool: True if the nested data is valid, False otherwise
        """
        if not isinstance(data, dtype) or not data:
            return False
        len_elem = None
        type_elem = None
        for elem in data:
            # Check size of nested
            if len_elem is None:
                len_elem = len(elem)
            elif len_elem != len(elem):
                print("test")
                return False
            # Check type of nested
            if type_elem is None:
                type_elem = type(elem)
            elif type_elem != type(elem):
                print("test2")
                return False
        return True

    def _check_shape(self, shape) -> bool:
        """ Make sure the given argument is a valid shape

        Args:
            shape (tuple): has to be a tuple of 2 positive ints

        Returns:
            bool: True if shape is valid, False otherwise
        """
        # Check valid tuples
        if not isinstance(shape, tuple) or len(shape) != 2:
            return False
        # Check elems are positive int
        for num in shape:
            if not isinstance(num, int) or num < 0:
                return False
        return True

    def from_list(self, lst, dtype=None):
        """ Converts a list to a numpy array with an optional specified data type.

        Args:
            lst: list of values that will be converted into a numpy array.
            dtype: optional: data type of the elements in the resulting NumPy array.

        Returns:
            NumPy array created from the input list.
            None if input is not valid.
        """
        if self._check_type(lst, list) is False:
            return None
        return np.array(lst, dtype)

    def from_tuple(self, tpl, dtype=None):
        """ Same as from_list but with a tuple """
        if not self._check_type(tpl, tuple):
            return None
        return np.array(tpl, dtype)

    def from_iterable(self, itr, dtype=None):
        """ Converts an iterable to a numpy array with an optional specified data type.

        Args:
            itr: iterable that will be converted into a numpy array.
            dtype: optional: data type of the elements in the resulting NumPy array.

        Returns:
            NumPy array created from the input iterable.
            None if input is not an iterable.
        """
        if not np.iterable(itr):
            return None
        return np.fromiter(itr, dtype)

    def from_shape(self, shape, value=0, dtype=float):
        """ Create a Numpy array with deesired shape and values.

        Args:
            shape: dimension of the array, has to be a tuple of positive int.
            value: optional: value to fill the array with, has to be a positive int.
            dtype: optional: data type of the elements in the NumPy array.

        Returns:
            NumPy array created from the input shape and value.
            None if input is not valid.
        """
        if not self._check_shape(shape):
            return None
        if not isinstance(value, int) or value < 0:
            return None
        return np.full(shape, value, dtype=dtype)

    def random(self, shape):
        """ Generate a Numpy array with the desired shape and random numbers

        Args:
            shape: dimension of the array, has to be a tuple of positive int.

        Returns:
            NumPy array created from the input shape.
            None if input is not valid.
        """
        if not self._check_shape(shape):
            return None
        return np.random.random(shape)

    def identity(self, num, dtype=None):
        """ Returns the identity matrix of a given size and data type

        Args:
            num: number of rows and columns in the identity matrix to be created.
            dtype: optional: data type of the elements in the matrix

        Returns:
            square identity matrix of size num
            None if input is not valid
        """
        if not isinstance(num, int) or num < 0:
            return None
        return np.identity(num, dtype)


if __name__ == "__main__":
    npc = NumPyCreator()

    """" ERROR TESTS, SHOULD RETURN NONE """
    # Not a list
    assert npc.from_list("toto") is None
    # Not homogeneous
    assert npc.from_list([]) is None
    # Not a tuple
    assert npc.from_tuple(3.2) is None
    # Not homogeneous
    assert npc.from_tuple(((1, 5, 8), (7, 5))) is None
    # Negative value
    assert npc.from_shape((-1, -1)) is None
    # Negative value
    assert npc.identity(-1) is None

    """ALL VALID TESTS"""

    # Expected: array([], shape=(2, 0), dtype=float64)
    print("Expected: array([], shape=(2, 0), dtype=float64)")
    result = repr(npc.from_list([[], []]))
    print(f"Result: {result}")
    print("-------------------------")

    # Expected: array([[1, 2, 3],
    #  [6, 3, 4],
    #  [8, 5, 6]])
    print("Expected: array([[1, 2, 3],\n\t[6, 3, 4],\n\t[8, 5, 6]])")
    result = repr(npc.from_list([[1, 2, 3], [6, 3, 4], [8, 5, 6]]))
    print(f"Result: {result}")
    print("-------------------------")

    # Expected: array(['a', 'b', 'c'], dtype='<U1')
    print("Expected: array(['a', 'b', 'c'], dtype='<U1')")
    result = repr(npc.from_tuple(("a", "b", "c")))
    print(f"Result: {result}")
    print("-------------------------")

    # Expected: array([0, 1, 2, 3, 4])
    print("Expected: array([0, 1, 2, 3, 4])")
    result = repr(npc.from_iterable(range(5)))
    print(f"Result: {result}")
    print("-------------------------")

    # Expected: array([], shape=(0, 0), dtype=float64)
    print("Expected: array([], shape=(0, 0), dtype=float64)")
    result = repr(npc.from_shape((0, 0)))
    print(f"Result: {result}")
    print("-------------------------")

    # Expected: array([[0., 0., 0., 0., 0.],
    #  [0., 0., 0., 0., 0.],
    #  [0., 0., 0., 0., 0.]])
    print(
        "Expected: array([[0., 0., 0., 0., 0.],\n\t[0., 0., 0., 0., 0.],\n\t[0., 0., 0., 0., 0.]]")
    result = repr(npc.from_shape((3, 5)))
    print(f"Result: {result}")
    print("-------------------------")

    # Expected: array([[0.74819604, 0.32295616, 0.27371925, 0.57171326, 0.92582071],
    #  [0.70307642, 0.94846695, 0.12465384, 0.25146454, 0.11179953],
    #  [0.38326719, 0.26179493, 0.88157011, 0.29978869, 0.72677049]])`
    print(
        "Expected: array([[rand, rand, rand, rand, rand],\n\t[rand, rand, rand, rand, rand],\n\t[rand, rand, rand, rand, rand]])")
    result = repr(npc.random((3, 5)))
    print(f"Result: {result}")
    print("-------------------------")

    # Expected: array([[1., 0., 0., 0.],
    #  [0., 1., 0., 0.],
    #  [0., 0., 1., 0.],
    #  [0., 0., 0., 1.]])
    print(
        "Expected: array([[1., 0., 0., 0.],\n\t[0., 1., 0., 0.],\n\t[0., 0., 1., 0.],\n\t[0., 0., 0., 1.]])")
    result = repr(npc.identity(4))
    print(f"Result: {result}")
    print("-------------------------")
