# Base declaration of our cookbook dictionary
cookbook = {}

def add_recipe_to_dict(name: str, ingr: list, meal: str, time: int,
                       print_usage: bool = True):
    """Adds our desired recipe to the cookbook

    Args:
        name (str, optional): Name of the recipe. Defaults to ''.
        ingr (list, optional): The list of ingredients. Defaults to [].
        meal (str, optional): The type of meal. Defaults to ''.
        time (int, optional): Time it takes in minutes. Defaults to 0.
        print_usage (bool, optional): . Defaults to True.
    """
    cookbook.update({name: {"ingredients": ingr, "meal": meal, "prep_time": time}})
    if print_usage is True:
        print(f"Successfully added '{name}' to our cookbook\n")

def add_recipe():
    """Asks for user input and call add_recipe_to_dict if all the information given is valid
    """
    name = str(input("What's the name of the recipe you want to add?\n> "))
    if name in cookbook:
        validation = input("Recipe already exists, do you want to update it? Type anything to continue or press Enter to go back to menu\n")
        if validation == '':
            return
    ingr = list(input("Enter the ingredients list in format 'ingr1 ingr2 ingr3'\n> ").split(" "))
    meal = str(input("What is the meal type ?\n> "))
    time = input("How many minutes does it take to prepare ?\n> ")
    while not time.isdigit():
            time = input("Incorrect format. Please just enter positive numbers\n> ")   
    add_recipe_to_dict(name, ingr, meal, int(time), True)

def delete_recipe():
    """Asks for user input and delete a recipe if it exists in cookbook dict.
    """
    name = str(input("Please enter the name of the recipe you want to delete\n> "))
    if name in cookbook:
        cookbook.pop(name)
        print(f"Successfully deleted recipe '{name}'")
    else:
        print("Recipe does not exist, try again")

def print_recipe():
    """Asks for user input and prints the details of a recipe if it exists in cookbook.
    """
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
        print_cookbook()
        return

def print_cookbook():
    """Print the recipe names if we have any in the cookbook. Otherwise, print an error message.
    """
    index = 1
    if not cookbook:
        print("Unlucky, our cookbook is empty, time to create new recipes!")
    else:
        print("Cookbook recipes:")
        for name in cookbook:
            print(f"\t{index} - {name}")
            index += 1

def quit_cookbook():
    """Print an exit message and pass. Program will exit the while loop just after.
    """
    print("\nCookbook Closed, see ya later !")
    pass

def print_usage():
    """Simply prints our options menu
    """
    usage = 'List of available options:\n'
    for key, value in options.items():
        usage += f"\t{key}: {value[0]}\n"
    print(usage, end='')

# Base declaration of our options dicitionary
options = {
    0: ["Print Usage", print_usage],
    1: ["Add a recipe", add_recipe],
    2: ["Delete a recipe", delete_recipe],
    3: ["Print a recipe", print_recipe],
    4: ["Print the cookbook", print_cookbook],
    5: ["Quit", quit_cookbook]
}

def handle_cookbook():
    """Loop until user enter 5 from main menu. If user enter a number between 0 and 4,
    call the appropriate function from our options dictionary.
    If user enters an invalid option, simply enter an error message and keep looping.
    """
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