import sys

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ':'/'}

def sos(args: list):
    """Parse arguments passed to function, then encode the resulting string into Morse.

    Args:
        args (list): List of strings to encode. Need to be alphanumeric or will throw KeyError.
    """
    if len(args) < 1:
        return("Usage: python sos.py <string1> <...>")
    result = []
    # Join all strings passed as arguments and make them uppercase
    args_string = ' '.join(args).upper()
    try:
        for letter in args_string:
            # Append to our result list the corresponding morse value for our current letter
            result.append(MORSE_CODE_DICT[letter])
        return(' '.join(result))
    except KeyError:
        return("Arguments need to be Alphanumeric to be translated.")

if __name__ == "__main__":
    result = sos(sys.argv[1:])
    print(result)