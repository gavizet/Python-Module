cookbook = {}

def add_recipe(recipe_name: str = '', ingredients: list = [], meal: str = '',\
    prep_time: int = 0, print_usage: bool = False):
    print("Adding recipe")
    pass

def delete_recipe(recipe_name):
    print("Deleting recipe")
    pass

def print_recipe(recipe_name):
    print("Printing recipe")
    pass

def print_cookbook():
    print("Printing cookbook")
    pass

def quit_cookbook():
    print("\nCookbook Closed, see ya later !")
    pass

def print_usage():
    print(f)

def handle_cookbook():
    add_recipe("Sandwich", ['ham', 'bread', 'cheese', 'tomatoes'], "lunch", 10)
    add_recipe("Cake", ['flour', 'sugar', 'eggs'], "dessert", 60)
    add_recipe("Salad", ['avocado', 'arugula', 'tomatoes', 'spinach'], "lunch", 15)
    
    options = {
        1: ["Add a recipe", add_recipe],
        2: ["Delete a recipe", delete_recipe],
        3: ["Print a recipe", print_recipe],
        4: ["Print the cookbook", print_cookbook],
        5: ["Quit", quit_cookbook]
    }
    action = None
    while action != 5:
        try:
            action = int(input(f"{print_usage()}"))
            operation = options.get(action)
            if operation:
                operation[1]()
            else:
                print("\nOption does not exist, please try again\n")
        except ValueError:
            print("\nOption does not exist, please try again\n")

if __name__ == "__main__":
    handle_cookbook()