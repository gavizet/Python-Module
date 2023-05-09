import pytest
from io import StringIO
from Module_00.ex_09.guess import guess_number

PARAMS = [
    (),
]

@pytest.mark.parametrize("args, expected", PARAMS)
def test_guess_number(args, expected):
    guess_number(42, 0)