"""Simple tests with print and asserts for Module_01/ex_01/game.py"""
from Module_01.ex_01.game import Stark

# To test, go into project root folder and use :
# 'python tests/Module_01/test_ex01.py'

if __name__ == "__main__":
    arya = Stark("Arya")
    print(arya.__dict__)

    print(f"Name is {arya.first_name} {arya.family_name}")
    # Prints the house words
    print("Arya's House Words are :", end='\r')
    arya.print_house_words()

    # True
    print(f"Is Arya alive : {arya.is_alive}")
    arya.die()
    print("Arya died")
    # False
    print(f"Is Arya alive : {arya.is_alive}")
