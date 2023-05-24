"""Write info about the @log decorated function into a machine.log file
This module is to learn about function decorators and wrappers, which will be used later on
to monitor function runtime or for debugging"""
import time
from random import randint
import os
import sys


def log(function):
    """
    Decorator function, usually used to monitor runtime of function calls or for debugging

    Args:
      function: The function that will be decorated with the `log` functionality.

    Returns:
      The `wrapper` function is being returned.
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper that logs the execution time of a given function and writes it to a file.

        Returns:
            The result of the function that is being passed as an argument to it.
        """
        start_time = time.time()
        func_result = function(*args, **kwargs)
        elapsed = time.time() - start_time
        username = os.getenv("USER", "user")
        func_name = function.__name__.replace('_', ' ').title()
        time_string = 's' if elapsed > 0.001 else 'ms'
        elapsed = elapsed if elapsed > 0.001 else elapsed * 1000
        with open("Module_02/ex_02/message.log", "a", encoding="utf-8") as file:
            file.write(
                f"({username}) Running: {func_name:19}"
                f"[ exec_time = {elapsed:.3f} {time_string:2} ]\n")
        return func_result
    return wrapper


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
