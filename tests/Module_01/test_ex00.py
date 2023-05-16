""""Some pytest parametrized tests to see if the error management for Recipe is properly handled"""
import pytest
from Module_01.ex_00.recipe import Recipe

PARAMS_RECIPE = [
    # No ingredient
    (["cooki", 2, 10, [],
     "deliciousness incarnate", "dessert"], AssertionError),
    # Difficulty not between 1 and 5
    (["cooki", 6, 10, ["dough", "sugar", "love"],
     "deliciousness incarnate", "dessert"], AssertionError),
    # Empty recipe name
    (["", 6, 10, ["dough", "sugar", "love"],
     "deliciousness incarnate", "dessert"], AssertionError),
    # Not a correct meal type
    (["cooki", 6, 10, ["dough", "sugar", "love"],
     "", "gouter"], AssertionError),
    # Int as recipe name
    ([123, 6, 10, ["dough", "sugar", "love"],
     "deliciousness incarnate", "dessert"], AssertionError),
    # Ok test
    (["cooki", 2, 10, ["dough", "sugar", "love"],
     "deliciousness incarnate", "dessert"], ""),
    # Ok test 2
    (["Italian Salad", 2, 20, ["Mozza", "Tomato", "Olive Oil"],
     "", "starter"], ""),
]


@pytest.mark.parametrize("args, expected", PARAMS_RECIPE)
def test_recipe_init(args, expected):
    """Test the error managemnt from the Recipe __init__ method.
    """
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            recipe = Recipe(*args)
    else:
        recipe = Recipe(*args)
        name, cooking_lvl, time, ingredients, description, meal_type = args
        assert recipe.name == name
        assert recipe.cooking_lvl == cooking_lvl
        assert recipe.cooking_time == time
        assert recipe.ingredients == ingredients
        assert recipe.description == description
        assert recipe.recipe_type == meal_type
