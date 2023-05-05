import sys


def odd_or_even(args):
    """Check if argument is valid (one number), then checks if it's zero, odd or even.

    Args:
        args (List): Arguments passed in the command line

    Raises:
        AssertionError: if more than one arg passed or argument is not a number
    """
    args_number = len(args)
    if args_number > 1:
        raise AssertionError("more than one argument are provided")
    elif args_number < 1:
        return("Usage: python whois.py <number>")
    elif not args[0].isdigit():
        raise AssertionError("argument is not an integer")
    number = int(args[0])
    if number == 0:
        return("I'm Zero.")
    elif (number % 2) == 0:
        return("I'm Even.")
    else:
        return("I'm Odd.")


if __name__ == "__main__":
    result = odd_or_even(sys.argv[1:])
    print(result)
