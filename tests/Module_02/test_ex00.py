import pytest
from Module_02.ex_00.ft_filter import ft_filter
from Module_02.ex_00.ft_map import ft_map
from Module_02.ex_00.ft_reduce import ft_reduce

PARAMS = [
    (),
]


@pytest.mark.parametrize("params, expected", PARAMS)
def test_map(params, expected):
    pass


@pytest.mark.parametrize("params, expected", PARAMS)
def test_filter(params, expected):
    pass


@pytest.mark.parametrize("params, expected", PARAMS)
def test_reduce(params, expected):
    pass
