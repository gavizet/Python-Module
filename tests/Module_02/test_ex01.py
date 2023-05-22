# You will find more tests in Module_02.ex_01.main
import pytest
from Module_02.ex_01.main import what_are_the_vars


PARAMS = [
    ([7], {}, {"var_0": 7}),
    ([None, []], {}, {"var_0": None, "var_1": []}),
    ([42], {'a': 10, 'var_0': 'world'}, None),
]


@pytest.mark.parametrize("args, kwargs, expected", PARAMS)
def test_what_are_the_vars(args, kwargs, expected):
    obj = what_are_the_vars(*args, **kwargs)
    if obj is None:
        assert obj == expected
    else:
        for key, value in vars(obj).items():
            assert value == expected[key]
