import pytest
from Module_01.ex_04.eval import Evaluator

PARAMS = [
    # Valid
    ([1.0, 2.0, 1.0, 4.0, 0.5], ["Le", "Lorem", "Ipsum", "est", "simple"], 32.0),
    # Error different size
    ([0.0, -1.0, 1.0, -12.0, 0.0, 42.42], ["Le", "Lorem", "Ipsum",\
                                           "n'", "est", "pas", "simple"], -1),
    # Error int in words
    ([1, 2, 3], ["word", 2, "wordo"], -1),
    # Error none types
    (None, None, -1),
    # Error empty arg
    ([1, 2, 3], [], -1),
]


@pytest.mark.parametrize("coefs, words, expected", PARAMS)
def test_evaluate(coefs, words, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            res_zip = Evaluator.zip_evaluate(coefs, words)
            res_enum = Evaluator.enumerate_evaluate(coefs, words)
    else:
        res_zip = Evaluator.zip_evaluate(coefs, words)
        res_enum = Evaluator.enumerate_evaluate(coefs, words)
        assert res_zip == res_enum
        assert res_zip == expected and res_enum == expected
