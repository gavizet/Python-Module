import pytest
from Module_03.ex_00.NumPyCreator import NumPyCreator
import numpy as np
import numpy.testing as npt

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
def test_error_arrays(params, expected):
    assert params == expected
