""""My own implementation of the filter built-in function"""


def ft_filter(function_to_apply, iterable):
    """Filter the function to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable. None if the iterable can not be used by the function.
    """
    try:
        for elem in iterable:
            if function_to_apply(elem):
                yield elem
    except TypeError as exception:
        print(str(exception))


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]

    # Expected: <generator object ft_filter at 0x7f709c777d00> # The adress will be different
    print(ft_filter(lambda dum: not (dum % 2), x))
    # Expected: [2, 4]
    print(list(ft_filter(lambda dum: not (dum % 2), x)))
    # Expected: []
    print(list(ft_filter(lambda dum: dum <= 1, [])))
    # Expected: Error
    print(ft_filter(function_to_apply=None, iterable=x))
    # Expected: Error
    list(ft_filter(function_to_apply=None, iterable=x))
