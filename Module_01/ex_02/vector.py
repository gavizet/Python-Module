"""
Ïntroduction to vectors and built-in methods, particularly ones allowing to perform operations
"""


class Vector:
    """Class to handle vector operations.
    Can add, radd, sub, rsub, mul, rmul, truediv, dot_product and transpose.
    """

    @staticmethod
    def is_row_vector_1_n(lst: list) -> bool:
        """Return True if the object is Row Vector : a list of a single list of several floats,
        False otherwise"""
        # Vector([[0.0, 1.0, 2.0, 3.0]])
        if not isinstance(lst, list) or len(lst) != 1:
            return False
        for number in lst[0]:
            if not isinstance(number, float):
                return False
        return True

    @staticmethod
    def is_column_vector_n_1(lst: list) -> bool:
        """"Return True if the object a Column Vector : a list of lists of a single float, False
        otherwise"""
        # Vector([[0.0], [1.0], [2.0], [3.0]])
        if not isinstance(lst, list) or len(lst) == 0:
            return False
        for sublist in lst:
            if not isinstance(sublist, list) or len(sublist) != 1\
                    or not isinstance(sublist[0], float):
                return False
        return True

    @staticmethod
    def is_int_vector(number: int) -> bool:
        """"Returns True if it's a positive number, False otherwise"""
        # Vector(5)
        if isinstance(number, int) and number > 0:
            return True
        return False

    @staticmethod
    def is_tuple_vector(tpl: tuple) -> bool:
        """"Returns True if it's a Tuple of 2 int where a < b"""
        # Vector((10, 16))
        if isinstance(tpl, tuple) and len(tpl) == 2 and tpl[0] <= tpl[1]\
                and isinstance(tpl[0], int) and isinstance(tpl[1], int):
            return True
        return False

    def __init__(self, values):
        self.values = []
        self.shape = ()
        if self.is_int_vector(values):
            self.shape = (values, 1)
            values = [[float(num)] for num in range(values)]
        elif self.is_tuple_vector(values):
            self.shape = (values[1] - values[0], 1)
            values = [[float(num)] for num in range(values[0], values[1])]
        elif self.is_row_vector_1_n(values):
            self.shape = (1, len(values[0]))
        elif self.is_column_vector_n_1(values):
            self.shape = (len(values), 1)
        else:
            raise ValueError(
                "A Vector can be defined as :\n\r\
                * List of a single list of several floats - [[0.0, 1.0, 2.0]]\n\r\
                * List of lists of a single float - Vector([[0.0], [1.0], [2.0]])\n\r\
                * Int > 0 (size) - Vector(5)\n\r\
                * Tuple of 2 ints (range) where a < b - Vector((6, 12))")
        self.values = values

    def dot_product(self, other):
        """Produces a dot product between two Vectors of the same shape"""
        if not isinstance(other, Vector) or self.shape != other.shape:
            raise ValueError(
                "Can only do the dot product with 2 Vectors of the same shape")
        result = 0
        for lst in range(self.shape[0]):
            for num in range(self.shape[1]):
                result += self.values[lst][num] * other.values[lst][num]
        return result

    def transpose(self):
        """Returns the transpose vector (i.e. a column vector into a row vector, or a row vector
        into a column vector)."""
        result = []
        if self.shape[0] <= 1:  # Row vector (one list of multiple floats)
            # Go through each nested list. Add each item of the sublist into a list of their own.
            result = [[item] for sublist in self.values for item in sublist]
        else:  # Column vector (multiple lists of a single float)
            # Go through each nested list. Add each item into one big list.
            result = [[item for sublist in self.values for item in sublist]]
        print(f"Result: {result}")
        return Vector(result)

    def __add__(self, other):
        if not isinstance(other, Vector) or self.shape != other.shape:
            raise ValueError("Can only add with 2 Vectors of the same shape")
        # Have to zip the list of list and then the lists themselves so we're able to
        # loop concurrently in self and other
        result = [[self_num + other_num for self_num, other_num in zip(self_lst, other_lst)]
                  for self_lst, other_lst in zip(self.values, other.values)]
        return Vector(result)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, Vector) or self.shape != other.shape:
            raise ValueError("Can only sub with 2 Vectors of the same shape")
        # Have to zip the list of list and then the lists themselves so we're able to
        # loop concurrently in self and other
        result = [[self_num - other_num for self_num, other_num in zip(self_lst, other_lst)]
                  for self_lst, other_lst in zip(self.values, other.values)]
        return Vector(result)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError("Can only multiply with int of float")
        # Could do double for loop with appends, or use deepcopy, but list comprehension
        # is the fastest for small-ish data sets
        result = [[num * other for num in lst] for lst in self.values]
        return Vector(result)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError("Can only divide with int of float")
        if other == 0:
            raise ValueError("Cannot divide by 0 you pleb")
        result = [[num / other for num in lst] for lst in self.values]
        return Vector(result)

    def __rtruediv__(self, other):
        raise ArithmeticError(
            "Division of a scalar by a Vector is not defined here.")

    def __str__(self):
        return f"Values: {str(self.values)} - Shape: {str(self.shape)}"

    def __repr__(self):
        return f"Values: {str(self.values)} - Shape: {str(self.shape)}"
