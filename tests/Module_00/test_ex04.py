import pytest
from Module_00.ex_04.operations import operations

def response_operations(add, sub, mul, div, mod):
    message = (
        f"Sum:\t\t{add}\n"
        f"Difference:\t{sub}\n"
        f"Produit:\t{mul}\n"
        f"Quotient:\t{div}\n"
        f"Modulo:\t\t{mod}\n"
    )
    return message

PARAMS = [
    (('', ''), "AssertionError: only integers\n"),
    (('12', 'test'), "AssertionError: only integers\n"),
    (('1', '2', '3'), "AssertionError: too many arguments\n"),
    ((), "Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3\n"),
    (('1', '0'),response_operations(1, 1, 0, "ERROR (division by 0)", "ERROR (modulo by 0)")),
    (('10', '3'), response_operations(13, 7, 30, 3.3333333333333335, 1)),
    (('42', '10'), response_operations(52, 32, 420, 4.2, 2)),
    (('42', '-10'), response_operations(32, 52, -420, -4.2, -8)),
]

@pytest.mark.parametrize("input, expected", PARAMS)
def test_operations(capsys, input, expected):
    operations(*input)
    captured_stdout, _ = capsys.readouterr()
    assert captured_stdout == expected