import pytest
from Module_02.ex_00.ft_filter import ft_filter
from Module_02.ex_00.ft_map import ft_map
from Module_02.ex_00.ft_reduce import ft_reduce

PARAMS_MAP = [
    (lambda i: i + 1, [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]),
    (lambda i: i ** 2, [1, 2, 3, 4, 5], [1, 4, 9, 16, 25]),
    (lambda x: x + 2, [], []),
    (None, [1, 2, 3, 4, 5], TypeError),
    (lambda x: x + 2, None, TypeError),
]


@pytest.mark.parametrize("function, iterable, expected", PARAMS_MAP)
def test_map(function, iterable, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            result = list(ft_map(function, iterable))
    else:
        result = list(ft_map(function, iterable))
        assert result == expected


PARAMS_FILTER = [
    (lambda i: not (i % 2), [1, 2, 3, 4, 5], [2, 4]),
    (lambda i: i <= 3, [1, 2, 3, 4, 5], [1, 2, 3]),
    (lambda i: i < 1, [1, 2, 3, 4, 5], []),
    (None, [1, 2, 3, 4, 5], TypeError),
    (lambda x: x + 2, None, TypeError),
]


@pytest.mark.parametrize("function, iterable, expected", PARAMS_FILTER)
def test_filter(function, iterable, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            result = list(ft_filter(function, iterable))
    else:
        result = list(ft_filter(function, iterable))
        assert result == expected


PARAMS_REDUCE = [
    (lambda x, y: x + y, ['H', 'e', 'l', 'l', 'o',
     ' ', 'W', 'o', 'r', 'l', 'd'], "Hello World"),
    (lambda x, y: x * y, [1, 2, 3, 4], 24),
    (lambda x, y: x / y, [16, 2, 2, 2], 2),
    (None, [1, 2, 3, 4, 5], TypeError),
    (lambda x: x + 2, None, TypeError),
]


@pytest.mark.parametrize("function, iterable, expected", PARAMS_REDUCE)
def test_reduce(function, iterable, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            result = ft_reduce(function, iterable)
    else:
        result = ft_reduce(function, iterable)
        assert result == expected
