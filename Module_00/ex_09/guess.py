import sys
from random import randint

def guess_number(num_to_find: int, attempts: int, print_usage: bool = True):
    attempts += 1
    user_input = ""
    if print_usage == True:
        print("Find the random number between 1 and 99. Type 'exit' to end the game")
    try:
        user_input = input("What's your guess between 1 and 99?\n> ")
        user_input = int(user_input)
        if int(user_input) < num_to_find:
            print("Too low!\n", end = '')
        elif int(user_input) > num_to_find:
            print("Too high!\n", end ='')
        else:
            if num_to_find == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if attempts == 1:
                print("First try, what a gamer!")
            else:
                print(f"Congratulations, you found {num_to_find} in {attempts} attempts!") 
            exit()  
    except ValueError:
        if user_input == 'exit':
            exit("Goodbye!")
        print("That's not a number")
    guess_number(num_to_find, attempts, False)

if __name__ == "__main__":
    num_to_find = randint(1, 99)
    guess_number(num_to_find, 0)