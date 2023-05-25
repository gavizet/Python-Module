import pytest
from Module_03.ex_00.NumPyCreator import NumPyCreator
import numpy as np

npc = NumPyCreator()

FAIL_PARAMS = [
    (npc.from_list("toto"), None),
    (npc.from_list([[1, 2, 3], [6, 3, 4], [8, 5, 6, 7]]), None),
    (npc.from_tuple(3.2), None),
    (npc.from_tuple(((1, 5, 8), (7, 5))), None),
    (npc.from_shape((-1, -1), 1), None),
    (npc.identity(-1), None),
]


@pytest.mark.parametrize("params, expected", FAIL_PARAMS)
def test_error_num_py_creator(params, expected):
    assert params == expected


VALID_PARAMS = [
    (npc.from_list([[], []]), "array([], shape=(2, 0), dtype=float64)"),
    (npc.from_list([[1, 2, 3], [6, 3, 4], [8, 5, 6]]),
     "array([[1, 2, 3], [6, 3, 4], [8, 5, 6]])"),
]


@pytest.mark.parametrize("params, expected", VALID_PARAMS)
def test_valid_num_py_creator(params, expected):
    pass
