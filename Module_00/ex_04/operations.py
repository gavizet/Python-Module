from re import A
import sys

def args_error(error_msg: str = ''):
    """Print desired error message

    Args:
        error_msg (str, optional): error message we wish to print. Defaults to ''.
    """
    if error_msg:
        print("AssertionError: {}".format(error_msg))
    else:
        print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")

def operations(*args) -> None:
    """Parse command line arguments. If 2 integers are given, print the addition, substraction,
    multiplication, division and modulo. Otherwise, call args_error with the desired message.
    """
    args_number = len(args)
    if args_number > 2:
        return(args_error("too many arguments"))
    elif args_number < 2:
        return(args_error())
    try:
        a = int(args[0])
        b = int(args[1])
        div_zero = "ERROR (division by 0)"
        mod_zero = "ERROR (modulo by 0)"
        message = (
            f"Sum:\t\t{a + b}\n"
            f"Difference:\t{a - b}\n"
            f"Produit:\t{a * b}\n"
            f"Quotient:\t{a / b if b != 0 else div_zero}\n"
            f"Modulo:\t\t{a % b if b != 0 else mod_zero}"
        )
        print(message)
    except ValueError:
        return(args_error("only integers"))

if __name__ == "__main__":
    result = operations(*sys.argv[1:])