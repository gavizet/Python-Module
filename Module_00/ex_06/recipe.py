cookbook = {}

def add_recipe_to_dict(name: str = '', ingr: list = [], meal: str = '',\
    time: int = 0, print_usage: bool = True):
    cookbook.update({name: {"ingredients": ingr, "meal": meal, "prep_time": time}})
    if print_usage is True:
        print(f"Successfully added '{name}' to our cookbook\n")

def add_recipe():
    name = str(input("What's the name of the recipe you want to add?\n> "))
    if name in cookbook:
        validation = input("Recipe already exists, do you want to update it? Type anything to continue or press Enter to go back to menu\n")
        if validation == '':
            return
    ingr = list(input("Enter the ingredients list in format 'ingr1 ingr2 ingr3'\n> ").split(" "))
    meal = str(input("What is the meal type ?\n> "))
    time = int(input ("How many minutes does it take to prepare ?\n> "))    
    add_recipe_to_dict(name, ingr, meal, time, True)

def delete_recipe(name: str = ''):
    name = str(input("Please enter the name of the recipe you want to delete\n> "))
    if name in cookbook:
        cookbook.pop(name)
        print(f"Successfully deleted recipe '{name}'")
    else:
        print("Recipe does not exist, try again")

def print_recipe(name: str = ''):
    name = str(input("Please enter the recipe's name to get its details\n> "))
    if name in cookbook:
        print(
            f"Recipe for {name}:\n",
            f"\tIngredients list: {cookbook[name]['ingredients']}\n",
            f"\tTo be eaten for {cookbook[name]['meal']}\n",
            f"\tTakes {cookbook[name]['prep_time']} minutes to prepare"
        )
    else:
        print("Recipe does not exist, try again.\n")
        return

def print_cookbook():
    index = 1
    if not cookbook:
        print("Unlucky, our cookbook is empty, time to create new recipes!")
    else:
        print("Cookbook recipes:")
        for name in cookbook:
            print(f"\t{index} - {name}")
            index += 1

def quit_cookbook():
    print("\nCookbook Closed, see ya later !")
    pass

def print_usage() -> None:
    usage = 'List of available options:\n'
    for key, value in options.items():
        usage += f"\t{key}: {value[0]}\n"
    print(usage, end='')

options = {
    0: ["Print Usage", print_usage],
    1: ["Add a recipe", add_recipe],
    2: ["Delete a recipe", delete_recipe],
    3: ["Print a recipe", print_recipe],
    4: ["Print the cookbook", print_cookbook],
    5: ["Quit", quit_cookbook]
}

def handle_cookbook():
    action = None
    print_usage()
    while action != 5:
        try:
            action = int(input("Please select an option (0 to see usage)\n> "))
            operation = options.get(action)
            if operation:
                operation[1]()
            else:
                print("\nOops, option does not exist.\n")
        except ValueError:
            print("\nOops, option does not exist.\n")

if __name__ == "__main__":
    add_recipe_to_dict("Sandwich", ['ham', 'bread', 'cheese', 'tomatoes'], "lunch", 10, False)
    add_recipe_to_dict("Cake", ['flour', 'sugar', 'eggs'], "dessert", 60, False)
    add_recipe_to_dict("Salad", ['avocado', 'arugula', 'tomatoes', 'spinach'], "lunch", 15, False)
    handle_cookbook()