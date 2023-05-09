import pytest
from Module_00.ex_06.recipe import handle_cookbook

PARAMS = [
    (),
]

@pytest.mark.parametrize("user_input, expected", PARAMS)
def test_recipe(user_input, expected):
    pass