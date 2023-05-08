import pytest
from Module_00.ex_05.kata00 import kata_00
from Module_00.ex_05.kata01 import kata_01
from Module_00.ex_05.kata02 import kata_02
from Module_00.ex_05.kata03 import kata_03
from Module_00.ex_05.kata04 import kata_04

PARAMS_KATA_00 = [
    ((), "The 0 numbers are: \n"),
    (("",42,21), "The 3 numbers are: , 42, 21\n"),
    ((0,0,0), "The 3 numbers are: 0, 0, 0\n"),
    ((19, 42, 21), "The 3 numbers are: 19, 42, 21\n"),
]

@pytest.mark.parametrize("input, expected", PARAMS_KATA_00)
def test_kata_00(capsys, input, expected):
    kata_00(input)
    captured_stdout, _ = capsys.readouterr()
    assert captured_stdout == expected

# =========================================================================== #

PARAMS_KATA_01 = [
    ({
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
     }, "Python was created by Guido van Rossum\nRuby was created by Yukihiro Matsumoto\nPHP was created by Rasmus Lerdorf\n"
    ),
    ({}, ""
    ),
    ({
        '1': 'me',
        '2': 'you',
        '3': 'them',
     }, "1 was created by me\n2 was created by you\n3 was created by them\n"
    )
]

@pytest.mark.parametrize("input, expected", PARAMS_KATA_01)
def test_kata_01(capsys, input, expected):
    kata_01(input)
    captured_stdout, _ = capsys.readouterr()
    assert captured_stdout == expected

# =========================================================================== #

PARAMS_KATA_02 = [
    ((2019, 9, 25, 3, 30), "09/25/2019 03:30\n"),
    ((19, 9, 25, 3, 300000), "09/25/0019 03:300000\n"),
]

@pytest.mark.parametrize("input, expected", PARAMS_KATA_02)
def test_kata_02(capsys, input, expected):
    kata_02(input)
    captured_stdout, _ = capsys.readouterr()
    assert captured_stdout == expected

# =========================================================================== #

PARAMS_KATA_03 = [
    ("The right format", "--------------------------The right format"),
    ("", "------------------------------------------"),
    ("          this is a test          ", "--------          this is a test          "),
    ("123456789012345678901234567890123456789012", "123456789012345678901234567890123456789012"),
]

@pytest.mark.parametrize("input, expected", PARAMS_KATA_03)
def test_kata_03(capsys, input, expected):
    kata_03(input)
    captured_stdout, _ = capsys.readouterr()
    assert captured_stdout == expected

# =========================================================================== #

PARAMS_KATA_04 = [
    ((0, 4, 132.42222, 10000, 12345.67), "module_00, ex_04 : 132.42, 1.00e+04, 1.23e+04\n"),
    ((1234567890, 0, -12, 45.45675, 12.123), "module_1234567890, ex_00 : -12.00, 4.55e+01, 1.21e+01\n")
]

@pytest.mark.parametrize("input, expected", PARAMS_KATA_04)
def test_kata_04(capsys, input, expected):
    kata_04(input)
    captured_stdout, _ = capsys.readouterr()
    assert captured_stdout == expected