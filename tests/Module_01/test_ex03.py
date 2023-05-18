import pytest
from Module_01.ex_03.generator import generator

TEXT_EASY = "This is a simple string for a basic test. Very simple."
TEXT_LATIN = "Le Lorem Ipsum est simplement du faux texte."
TEXT_PONCT = "We li@ke ran@dom pon@ctua@tion"

PARAMS = [
    (12, " ", None, ["ERROR"]),  # Text not str
    (TEXT_EASY, 12, None, ["ERROR"]),  # Sep not str
    (TEXT_EASY, "si", "test", ["ERROR"]),  # Not an option
    (TEXT_EASY, " ", None, ['This', 'is', 'a', 'simple',
     'string', 'for', 'a', 'basic', 'test.', 'Very', 'simple.']),
    (TEXT_EASY, ".", None, ['This is a simple string for a basic test',\
                            ' Very simple', '']),
    (TEXT_EASY, "i", None, ['Th', 's ', 's a s', 'mple str', 'ng for a bas',\
                            'c test. Very s', 'mple.']),
    (TEXT_EASY, "si", None, ['This is a ', 'mple string for a ba',\
                             'c test. Very ', 'mple.']),
    (TEXT_LATIN, " ", None, ["Le", "Lorem", "Ipsum", "est", "simplement",\
                             "du", "faux", "texte."]),
    (TEXT_LATIN, " ", "ordered", ["Ipsum", "Le", "Lorem", "du", "est", "faux",\
                                  "simplement", "texte."]),
    ("a b c d e e c a""", " ", "unique", ["a", "b", "c", "d", "e"]),
]

# I cba writing deep tests for the shuffle, just test manually


@pytest.mark.parametrize("text, sep, opt, expected", PARAMS)
def test_generator(text, sep, opt, expected):
    result = []
    for word in generator(text, sep, opt):
        result.append(word)
    assert result == expected
