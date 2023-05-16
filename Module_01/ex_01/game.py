"""Module to tackle the notion of class inheritance"""


class GotCharacter:
    """Generic class representing a Game of Thrones character"""

    def __init__(self, first_name: str = None, is_alive: bool = True) -> None:
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """Represents the Stark family

    Args:
        GotCharacter (class): the parent Class
    """

    def __init__(self, first_name: str = None, is_alive: bool = True) -> None:
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        """Prints the motto of the Stark house"""
        print(self.house_words)

    def die(self):
        """Change parent class attribute is_alive to False"""
        self.is_alive = False
