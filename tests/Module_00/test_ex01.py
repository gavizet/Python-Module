import pytest
from Module_00.ex_01.exec import reverse_string


@pytest.mark.parametrize("args, result",
                         [([""], ""),  # One empty arg
                          (["Hello"], "OLLEh"),  # One normal arg
                          (["L337 5P3AK!"], "!ka3p5 733l"),  # One harder arg
                          (['L337', '5P3AK!'], "!ka3p5 733l"),  # Multiple args
                          # Multiple args with one empty
                          (['L337', '', '5P3AK!'], "!ka3p5 733l"),
                          (['', '', ''], ""),  # Multiple empty args
                          # Multiple args filled with spaces
                          ([' ', '   ', '     '], "")
                          ]
                         )
def test_reverse_string(args, result):
    expected = reverse_string(args)
    assert expected == result
