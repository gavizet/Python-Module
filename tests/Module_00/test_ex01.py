import unittest
from Module_00.ex_01.exec import reverse_string


class Test(unittest.TestCase):
    test_cases = [
        ([""], ""),
        (["Hello"], "OLLEh"),
        (["L337 5P3AK!"], "!ka3p5 733l"),
        (['L337', '5P3AK!'], "!ka3p5 733l"),
        (['L337', '', '5P3AK!'], "!ka3p5 733l"),
        (['', '', ''], "")
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
