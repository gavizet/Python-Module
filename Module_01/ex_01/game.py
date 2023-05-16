"""Module to tackle the notion of class inheritance"""


class GotCharacter:
    """Base class with 2 attributes on __init__"""

    def __init__(self, first_name, is_alive=True) -> None:
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """Sublass Stark that inherits from GotCharacter and it's __init__ method

    Args:
        GotCharacter (class): the parent Class
    """

    def __init__(self, first_name=None, is_alive=True) -> None:
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        """Prints the motto of the Stark house"""
        print(self.house_words)

    def die(self):
        """Change parent class attribute is_alive to False"""
        self.is_alive = False
