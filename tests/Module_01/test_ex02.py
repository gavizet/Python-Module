import pytest
from Module_01.ex_02.vector import Vector

VECTORS_INIT = [
    ("stupid test", ValueError),  # Error string
    (-3, ValueError),  # Error negative int
    ((10, 6), ValueError),  # Error tuple with a > b
    ([0.0, 1.0, 2.0, 3.0], ValueError),  # Error list of floats
    ([[0.0, 1.0], [2.0, 3.0]], ValueError),  # Error > than 1 float/sublist
    ([[]], [[[]], (1, 0)]),  # Valid, gives empty values
    ((1, 1), [[], (0, 1)]),  # Valid, gives empty values
    (4, [[[0.0], [1.0], [2.0], [3.0]], (4, 1)]),  # Valid int
    ((6, 10), [[[6.0], [7.0], [8.0], [9.0]], (4, 1)]),  # Valid tuple
    ([[1.0, 2.0, 3.0]], [[[1.0, 2.0, 3.0]], (1, 3)]),  # Valid row
    ([[1.0], [2.0], [3.0]], [[[1.0], [2.0], [3.0]], (3, 1)]),  # Valid column
]


@pytest.mark.parametrize("args, expected", VECTORS_INIT)
def test_vector_init(args, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            vector = Vector(args)
    else:
        vector = Vector(args)
        assert vector.values == expected[0]
        assert vector.shape == expected[1]


VECTOR_ADD_SUB = [
    (Vector(4), 2, ValueError),  # Error add by scalar
    (Vector(4), Vector((10, 16)), ValueError),  # Error different shape
    (Vector(4), Vector([[1.0], [1.0], [1.0], [1.0]]),
     [[1.0], [2.0], [3.0], [4.0]]),  # Valid add
    (Vector(4), Vector(4), [[0.0], [2.0], [4.0], [6.0]]),  # Valid add
    (Vector(4), Vector([[1.0], [1.0], [1.0], [1.0]]),
     [[-1.0], [0.0], [1.0], [2.0]]),  # Valid sub
    (Vector(4), Vector(4), [[0.0], [0.0], [0.0], [0.0]]),  # Valid sub
]


@pytest.mark.parametrize("vector, other, expected", VECTOR_ADD_SUB)
def test_vector_add_sub(vector, other, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            vector + other
            vector - other
    else:
        add = vector + other
        sub = vector - other
        assert expected in (add.values, sub.values)


VECTOR_MUL_DIV = [
    (Vector(4), 0, ValueError),  # Error, div by 0
    (Vector(4), None, ValueError),  # Error, div by None
    (3, Vector(4), ArithmeticError),  # Error, rdiv not handled
    (Vector(4), Vector((10, 16)), ValueError),  # Error, mult by Vector
    (Vector(4), "test", ValueError),  # Error, mult by string
    (Vector(4), 2, [[0.0], [2.0], [4.0], [6.0]]),  # Valid int mul
    (Vector(4), 2, [[0.0], [0.5], [1.0], [1.5]]),  # Valid int div
    (Vector(4), 2.0, [[0.0], [2.0], [4.0], [6.0]]),  # Valid float mul
    (Vector(4), 2.0, [[0.0], [0.5], [1.0], [1.5]]),  # Valid float div
]


@pytest.mark.parametrize("vector, other, expected", VECTOR_MUL_DIV)
def test_vector_mul_div(vector, other, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            vector * other
            vector / other
    else:
        mul = vector * other
        div = vector / other
        assert expected in (mul.values, div.values)


VECTOR_DOT_PRODUCT = [
    (Vector(4), 4, ValueError),  # Error, can only dot 2 vectors
    (Vector(4), Vector((10, 16)), ValueError),  # Error, diff shape vectors
    (Vector(4), Vector(4), 14),
    (Vector([[0.0], [1.0], [2.0], [3.0]]),
     Vector([[2.0], [1.5], [2.25], [4.0]]), 18),
    (Vector((6, 10)), Vector((6, 10)), 230),
]


@pytest.mark.parametrize("vector, other, expected", VECTOR_DOT_PRODUCT)
def test_vector_dot_product(vector, other, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            vector.dot_product(other)
            other.dot_product(vector)
    else:
        assert vector.dot_product(other) == expected
        assert other.dot_product(vector) == expected


VECTOR_TRANSPOSE = [
    (Vector(4), [[0.0, 1.0, 2.0, 3.0]]),
    (Vector((6, 10)), [[6.0, 7.0, 8.0, 9.0]]),
    (Vector([[0.0, 1.0, 2.0, 3.0]]), [[0.0], [1.0], [2.0], [3.0]]),
    (Vector([[0.0], [1.0], [2.0], [3.0]]), [[0.0, 1.0, 2.0, 3.0]]),
]


@pytest.mark.parametrize("vector, expected", VECTOR_TRANSPOSE)
def test_vector_transpose(vector, expected):
    transposed = vector.transpose()
    assert transposed.values == expected
    assert transposed.shape[0] == vector.shape[1]
    assert transposed.shape[1] == vector.shape[0]
