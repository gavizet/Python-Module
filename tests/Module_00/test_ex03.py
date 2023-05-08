import pytest
from Module_00.ex_03.count import text_analyzer

long_text1 = "Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles."
long_text2 = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace."

response_text = "The text contains {} characters:\n- {} upper letters\n- {} lower letters\n- {} punctuation marks\n- {} spaces\n"

def response_text_analyzer(chars_num, upper, lower, punct, space):
    return(response_text.format(chars_num, upper, lower, punct, space))

PARAMS = [
    (('Hello World!', 'test'), "Error: more than one argument are provided\n"), # Too many arguments
    ([42], "AssertionError: argument is not a string\n"),                       # Arg is not a string
    ([""], response_text_analyzer(0, 0, 0, 0, 0)),                              # Empty but valid arg
    (["Hello World!"], response_text_analyzer(12, 2, 8, 1, 1)),                 # Simple string
    ([long_text1], response_text_analyzer(143, 2, 113, 4, 18)),                 # Long string
    ([long_text2], response_text_analyzer(234, 5, 187, 8, 30)),                 # Even longer string
]

@pytest.mark.parametrize("args_input, expected", PARAMS)
def test_text_analyzer(capsys, args_input, expected):
    text_analyzer(*args_input)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == expected
    