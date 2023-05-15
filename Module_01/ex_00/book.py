from datetime import datetime
from Module_01.ex_00.recipe import Recipe


class Book:

    def __init__(self, name="Recipe Cookbook"):
        try:
            self.name = str(name)
            self.creation_date = datetime.now()
            self.last_update = self.creation_date
            self.recipes_list = {"starter": [], "lunch": [], "dessert": []}
        except ValueError:
            print("Error : wrong arguments")

    def get_recipe_by_name(self, name: str):
        """Prints a recipe with the name and returns the instance

        Args:
                name (str): the name of the recipe to print
        """
        for recipes in self.recipes_list.values():
            for recipe in recipes:
                if recipe.name == name:
                    print(recipe.name)
                    return recipe
        return "Recipe does not exist, try again."

    def get_recipes_by_types(self, recipe_type: str):
        """Get all recipe names for a given recipe type

        Args:
            recipe_type (str): the type of recipe we want to filter on
        """
        if recipe_type not in self.recipes_list.keys():
            raise AssertionError(
                f"Recipe type needs to be one of {', '.join(self.recipes_list)}")
        all_desired_meals = []
        for meal_type_list in self.recipes_list[recipe_type]:
            all_desired_meals.append(meal_type_list.name)
        return all_desired_meals

    def add_recipe(self, recipe: Recipe):
        """Add a recipe to the book and update last_update

        Args:
            recipe (class object): the Recipe object we want to add
        """
        if not isinstance(recipe, Recipe):
            raise AssertionError("That's not a Recipe object")
        self.last_update = datetime.now()
        self.recipes_list[recipe.recipe_type].append(recipe)
