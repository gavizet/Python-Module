"""The goal of the exercise is to discover the concept of generator object"""
from random import randint


def shuffle(lst: list) -> list:
    """Returns a randomly shuffled list of words
    Random shuffle module not allowed, using Fisher-Yates's shuffle algorithm"""
    # Need the -1 for len otherwise it go   es out of range
    for index in range(len(lst)-1, 0, -1):
        rand_int = randint(0, index)
        # Swap in place based between index and the randint
        lst[index], lst[rand_int] = lst[rand_int], lst[index]
    return lst


def unique(lst: list) -> list:
    """Returns a new list without any doublons"""
    result = []
    [result.append(word) for word in lst if word not in result]
    return result


def ordered(lst: list) -> list:
    """Returns a sorted list"""
    return sorted(lst)


OPTIONS = {
    "shuffle": shuffle,
    "unique": unique,
    "ordered": ordered,
}


def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.

    Args:
            text (_type_): Text to be worked on
            sep (str, optional): _description_. Defaults to ' '. Separator used to create the substrings.
            option (str, optional): Precise if an action is to be performed to the substrings. Defaults to None.

    Returns:
            list: The list of substrings we performed options on
    """
    if not isinstance(text, str) or not isinstance(sep, str) or\
            option not in ["shuffle", "unique", "ordered", None]:
        yield "ERROR"
        return
    lst = text.split(sep)
    if option is not None:
        option_function = OPTIONS.get(option)
        lst = option_function(lst)
    for substring in lst:
        yield substring


if __name__ == "__main__":
    TEST = "This is a simple string for a basic test. Very simple."
    RES = []
    print("======= NO OPTION ========")
    for word in generator(TEST, sep=" "):
        RES.append(word)
    print(RES)
    print("------------------------------------")

    RES = []
    print("======= ORDERED ========")
    for word in generator(TEST, option="ordered"):
        RES.append(word)
    print(RES)
    print("------------------------------------")

    RES = []
    print("======= UNIQUE ========")
    for word in generator(TEST, option="unique"):
        RES.append(word)
    print(RES)
    print("------------------------------------")

    RES = []
    print("======= SHUFFLE ========")
    for word in generator(TEST, option="shuffle"):
        RES.append(word)
    print(RES)
    print("------------------------------------")

    RES = []
