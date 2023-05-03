import sys


def reverse_string(all_args):
    """Join list into string, reverse it, swap the case and return the resulting string.

    Args:
        all_args (list): list of arguments passed to the command line
    """
    # Delete empty args, then join with whitespace separator
    args = " ".join([arg for arg in all_args if arg])
    # Reverse string, swap the case then delete leading and ending spaces
    result = args[::-1].strip().swapcase()
    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        result = "Usage: python exec.py 'string1' 'other string'"
    else:
        result = reverse_string(sys.argv[1:])
    print(result)
