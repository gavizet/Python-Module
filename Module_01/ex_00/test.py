"""
Simple test file that simulates the creation of a Book and the usage of
its different methods
"""
from book import Book
from recipe import Recipe

# See tests/Module_01/test_ex00.py for tests on the Recipe class
# They're done with pytest and can just be launched with all the rest from the
# root folder with '/pytest'

if __name__ == "__main__":
    salad = Recipe("Salad", 1, 10, [
                   "tomato", "cheese", "leafy greens"], "Yes.", "starter")
    pasta = Recipe("Pasta", 1, 15, [
                   "pasta", "cheese", "tomato"], "No.", "lunch")
    meat = Recipe("Meat", 3, 30, ["beef", "butter",
                  "onions"], "juicy steak", "lunch")
    cake = Recipe("Cake", 3, 60, ["dough", "sugar",
                  "chocolate"], "chocolate cake", "dessert")

    book = Book()
    assert book.name == "Recipe Cookbook"

    book.add_recipe(salad)
    print("Salad recipe added")
    print("==================================")
    book.add_recipe(pasta)
    print("Pasta recipe added")
    print("==================================")
    book.add_recipe(meat)
    print("Meat recipe added")
    print("==================================")
    book.add_recipe(cake)
    print("Cake recipe added")
    print("==================================")
    # Returns an error message because not a valid Recipe
    print(book.add_recipe("Not a Recipe object"))
    print("==================================")

    get_salad = book.get_recipe_by_name("Salad")
    print(f"Get salad returned : {get_salad}")
    print("==================================")
    get_pasta = book.get_recipe_by_name("Pasta")
    print(f"Get pasta returned : {get_pasta}")
    print("==================================")
    get_meat = book.get_recipe_by_name("Meat")
    print(f"Get meat returned : {get_meat}")
    print("==================================")
    get_cake = book.get_recipe_by_name("Cake")
    print(f"Get cake returned : {get_cake}")
    print("==================================")
    get_non_recipe = book.get_recipe_by_name("Not a Recipe")
    print(f"Get non recipe returned : {get_non_recipe}")
    print("==================================")
    assert get_non_recipe == "Recipe does not exist, try again."

    get_starters = book.get_recipes_by_types("starter")
    print(f"Get starters returned : {get_starters}")
    print("==================================")
    get_lunches = book.get_recipes_by_types("lunch")
    print(f"Get lunches returned : {get_lunches}")
    print("==================================")
    get_desserts = book.get_recipes_by_types("dessert")
    print(f"Get desserts returned : {get_desserts}")
    print("==================================")
    get_non_type = book.get_recipes_by_types("Not a type")
    print(f"Get non type returned : {get_non_type}")
    print("==================================")
    assert get_non_type == "Recipe type needs to be one of starter, lunch, dessert"
