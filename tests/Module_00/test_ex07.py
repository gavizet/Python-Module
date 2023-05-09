import pytest
from Module_00.ex_07.filterwords import filterwords

long_ass_string = 'A robot must protect its own existence as long as such protection does not conflict with the First or Second Law'
usage = "\n\tUsage: python filterwords.py <string> <number>"
too_many_args = "Too many arguments." + usage
too_few_args = "Not enough arguments." + usage
wrong_arg_type = "Wrong argument type." + usage


PARAMS = [
    (['test', '1', '1'], too_many_args), # Too many arguments
    (['1'], too_few_args), # Not enough arguments
    (['1', '1'], wrong_arg_type), # Wrong type of argument 1
    (['1', 'test'], wrong_arg_type), # Wrong type of argument 2
    (['', '3'], []), # Empty string
    (['Hello', '3'], ['Hello']), # One word
    (['Hello my friend', '5'], ['friend']), # String of multiple words
    ([long_ass_string, '6'], ['protect', 'existence', 'protection', 'conflict']), # Long ass string
    (['Hello my friend !@#$,;', '5'], ['friend']), # String of multiple words and punctuation
    (['Hello, my fri,end', '5'], ['friend']), # String of multiple words and punctuation within words
    (['!#;.,', '3'], []), # String of only punctuation
    (['Hello my friend', '10'], []), # String of valid arguments that output empty array
]

@pytest.mark.parametrize("args, expected", PARAMS)
def test_filterwords(args, expected):
    result = filterwords(args)
    assert result == expected