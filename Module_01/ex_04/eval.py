"""The goal is to discover zip and enumerate. Woah."""


def check_arguments_valid(coefs, words) -> bool:
    """Makes sure both arguments are lists of the same size with :
        coefs : list of int or float
        words : list of str
    """
    if not isinstance(coefs, list) or not isinstance(words, list):
        return False
    if len(coefs) != len(words):
        return False
    if not all([isinstance(word, str) for word in words]):
        return False
    if not all([isinstance(num, (int, float)) for num in coefs]):
        return False
    return True


class Evaluator:
    """This is an evaluator. Yay"""

    @staticmethod
    def zip_evaluate(coefs, words):
        """Evaluate a list of int and a list of str with zip"""
        if not check_arguments_valid(coefs, words):
            return -1
        result = sum([num * len(word) for num, word in zip(coefs, words)])
        return result

    @staticmethod
    def enumerate_evaluate(coefs, words):
        """Evaluate a list of int and a list of str with enumerate"""
        if not check_arguments_valid(coefs, words):
            return -1
        result = sum([coefs[index] * len(word)
                     for index, word in enumerate(words)])
        return result


if __name__ == "__main__":
    def test_evaluate(coefs, words):
        """Test function"""
        print(f"Test for {coefs}/{words}:")
        print(Evaluator.enumerate_evaluate(coefs, words))
        print(Evaluator.zip_evaluate(coefs, words))
        print()

    test_evaluate([1.0, 2.0, 1.0, 4.0, 0.5], [
                  "Le", "Lorem", "Ipsum", "est", "simple"])
    test_evaluate([0.0, -1.0, 1.0, -12.0, 0.0, 42.42],
                  ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"])
