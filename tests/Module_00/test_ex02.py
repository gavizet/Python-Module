import pytest
from Module_00.ex_02.whois import odd_or_even

test_data = [
    (["2"], "I'm Even."),                       # Valid even
    (["24546456546546"], "I'm Even."),          # Valid even big int
    (["-2"], AssertionError),                   # Unalid negative even
    (["1"], "I'm Odd."),                        # Valid odd
    (["-1"], AssertionError),                   # Unvalid negative odd
    (["0"], "I'm Zero."),                       # Valid zero
    (["3,33"], AssertionError),                 # Unvalid float
    (["test"], AssertionError),                 # Unvalid string
    (["   "], AssertionError),                  # Unvalid empty arg
    (["12", "-12"], AssertionError),            # Unvalid more than one arg
    ([], "Usage: python whois.py <number>"),    # Unvalid no arg
]


def check(function, expected, args=(), kwargs={}):
    if type(expected) == type and issubclass(expected, Exception):
        with pytest.raises(expected):
            function(*args, **kwargs)
    else:
        assert function(*args, **kwargs) == expected


@pytest.mark.parametrize("args, expected", test_data)
def test_odd_or_even(args, expected):
    check(odd_or_even, expected, (args,))
    # if type(expected) == type and issubclass(expected, Exception):
    #    with pytest.raises(expected):
    #        odd_or_even(args)
    # else:
    #    assert odd_or_even(args) == expected
