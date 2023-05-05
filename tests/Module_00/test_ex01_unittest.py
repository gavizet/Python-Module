import unittest
from Module_00.ex_01.exec import reverse_string

# Just some example tests with unittest, but overrall will use Pytest throughout the project


class Test(unittest.TestCase):
    test_cases = [
        # One empty arg
        ([""], ""),
        # One normal arg
        (["Hello"], "OLLEh"),
        # One harder arg
        (["L337 5P3AK!"], "!ka3p5 733l"),
        # Multiple args
        (['L337', '5P3AK!'], "!ka3p5 733l"),
        # Multiple args with one empty
        (['L337', '', '5P3AK!'], "!ka3p5 733l"),
        # Multiple empty args
        (['', '', ''], ""),
        # Multi args filled with spaces
        ([' ', '   ', '     '], "")
    ]

    test_functions = [
        reverse_string
    ]

    def test_reverse_string(self):
        for f in self.test_functions:
            for parameter, expected_result in self.test_cases:
                assert f(parameter) == expected_result


if __name__ == "__main__":
    unittest.main()
