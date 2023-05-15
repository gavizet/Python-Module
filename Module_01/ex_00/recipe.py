import sys


class Recipe:
    """The Recipe class defines a recipe object with multiple attributes to describe it and 
    a method to display a recipe.
    """

    def __init__(self, name: str, cooking_lvl: int, cooking_time: int,
                 ingredients: list, description: str, recipe_type: str):
        """Initialize the recipe object with all the given parameters after checking they are
        valid.

        Args:
            name (str): the name of the recipe
            cooking_lvl (int): difficulty of the recipe, between 1 and 5
            cooking_time (int): time to cook the recipe in minutes
            ingredients (list): list of ingredients, must not be empty
            description (str): simple text, only argument that can be empty
            recipe_type (str): has to be 'starter' 'lunch' or 'dessert'

        Raises:
            AssertionError: raised if any of the given parameters are invalid.
        """
        try:
            self.name = str(name)
            self.cooking_lvl = int(cooking_lvl)
            self.cooking_time = int(cooking_time)
            self.ingredients = list(ingredients)
            self.description = str(description)
            self.recipe_type = str(recipe_type)
            if not isinstance(name, str) or len(name) < 1:
                raise AssertionError("Name of the recipe needs to be a string")
            elif cooking_lvl < 1 or cooking_lvl > 5:
                raise AssertionError(
                    "Cooking level needs to be between 1 and 5")
            elif cooking_time < 0:
                raise AssertionError(
                    "I didn't know it was possible to have negative cooking")
            elif len(ingredients) == 0:
                raise AssertionError("Ingredients list cannot be empty")
            elif recipe_type not in ['starter', 'lunch', 'dessert']:
                raise AssertionError(
                    "Recipe can only be a starter, lunch or dessert")
        except (ValueError) as exception:
            print("Error: ", exception)
            sys.exit()

    def __str__(self):
        """Simply returns a recipe text describing our Recipe object

        Returns:
            str: nicely formated recipe text
        """
        recipe_text = (
            f"{self.name}: \n"
            f"\rDifficulty: {self.cooking_lvl}/5\n"
            f"\rPreparation time: {self.cooking_time}\n"
            f"\rIngredients : {', '.join(self.ingredients)}\n"
            f"\rMeal : {self.recipe_type}\n"
            f"\r\nDescription: {self.description}"
        )
        return recipe_text
