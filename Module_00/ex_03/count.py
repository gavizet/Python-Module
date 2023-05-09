import sys
import re


def regex(text):
    """Simple regex function that prints our count result

    Args:
        text (str): Valid argument passed to text_analyzer
    """
    length = len(text)
    upper = len(re.findall(r'[A-Z]', text))
    lower = len(re.findall(r'[a-z]', text))
    punct = len(re.findall(r'(\.|\-|\'|,|:|;|!)', text))
    space = len(re.findall(r'[\s]', text))

    print("The text contains {} characters:".format(length))
    print("- {} upper letters".format(upper))
    print("- {} lower letters".format(lower))
    print("- {} punctuation marks".format(punct))
    print("- {} spaces".format(space))


def text_analyzer(*args) -> None:
    """Takes a list of arguments as parameter. If the argument is valid (1 string arg), parses it and prints
    the number of lower, upper, punct and space characters that the text contains.
    """
    args_num = len(args)
    if args_num == 0:
        text = str(input("What is the text to analyze ?\n"))
        return(regex(text))
    elif args_num > 1:
        print("Error: more than one argument are provided")
        return
    elif not isinstance(args[0], str):
        print("AssertionError: argument is not a string")
        return
    text = args[0]
    regex(text)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        text_analyzer()
    else:
        text_analyzer(*sys.argv[1:])
