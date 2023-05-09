import sys
import string

def print_error_msg(message: str):
    return(f"{message}\n\tUsage: python filterwords.py <string> <number>")

def filterwords(args):
    """Parse our arguments, remove all punctuation from S and
    returns the list of words in S that contains more than N characters

    Args:
        args (list): our list of arguments from sys.argv[1:]

    Returns:
        list: Our list of words that are longer than N characters
    """
    args_num = len(args)
    # Parse args
    if args_num < 2:
        return(print_error_msg("Not enough arguments."))
    elif args_num > 2:
        return(print_error_msg("Too many arguments."))
    elif args[0].isdigit() or not args[1].isdigit():
        return(print_error_msg("Wrong argument type."))
    
    # Replace all punctuation characters with a space. See makestrans and translate methods
    string_without_punct = args[0].translate(str.maketrans('', '', string.punctuation))
    
    # Split into list on space character
    my_list = string_without_punct.split(" ")
    
    # Put every word > n characters into our result list
    result = [word for word in my_list if len(word) > int(args[1])]
    return result

if __name__ == "__main__":
    result = filterwords(sys.argv[1:])
    print(result)