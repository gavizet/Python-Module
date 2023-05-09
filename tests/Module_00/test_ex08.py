import pytest
from Module_00.ex_08.sos import sos

PARAMS = [
    ([], "Usage: python sos.py <string1> <...>"), # No argument
    (['', '', ''], '/ /'), # Multiple empty strings
    ([''], ''), # Empty string
    (['SOS'], "... --- ..."), # Uppercase word
    (['sos'], "... --- ..."), # Lowercase word
    (['69'], "-.... ----."), # Numbers
    (['6    9'], "-.... / / / / ----."), # Numbers with spaces
    (['a1 B2', 'c3D4e5F6'], ".- .---- / -... ..--- / -.-. ...-- -.. ....- . ..... ..-. -...."), # 2 words of alphanumeric
    (['He||o'], "Arguments need to be Alphanumeric to be translated."), # Non alphanumeric string
    (['96 BOULEVARD', 'Bessiere'], "----. -.... / -... --- ..- .-.. . ...- .- .-. -.. / -... . ... ... .. . .-. ."), # Basic strings
]

@pytest.mark.parametrize("args, expected", PARAMS)
def test_sos(args, expected):
    result = sos(args)
    assert result == expected