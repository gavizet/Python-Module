import statistics
import pytest
from Module_02.ex_05.TinyStatistician import TinyStatistician

PARAMS = [
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5, 6, 7],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [0, 7, 13, 16, 21, 32, 46, 82, 85, 100],
    [1, 10, 15, 20, 42, 59, 300],
    [1, 10, 42, 59, 300],
]


@pytest.mark.parametrize("params", PARAMS)
def test_mean(params):
    my_stats = TinyStatistician()
    assert my_stats.mean(params) == statistics.mean(params)


@pytest.mark.parametrize("params", PARAMS)
def test_median(params):
    my_stats = TinyStatistician()
    assert my_stats.median(params) == statistics.median(params)


@pytest.mark.parametrize("params", PARAMS)
def test_var(params):
    my_stats = TinyStatistician()
    assert my_stats.var(params) == statistics.pvariance(params) or round(
        my_stats.var(params), 2) == statistics.pvariance(params)


@pytest.mark.parametrize("params", PARAMS)
def test_std(params):
    my_stats = TinyStatistician()
    assert my_stats.std(params) == statistics.pstdev(params)


QUARTILE_PARAMS = [
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [2.5, 8.5]),
    ([1, 42, 300, 10, 59], [5.5, 179.5]),
    ([0, 20, 40, 60, 80, 100], [20.0, 80.0]),
    ([0, 25, 50, 75, 100], [12.5, 87.5]),
]


@pytest.mark.parametrize("params, expected", QUARTILE_PARAMS)
def test_quartile(params, expected):
    my_stats = TinyStatistician()
    assert my_stats.quartiles(params) == expected
