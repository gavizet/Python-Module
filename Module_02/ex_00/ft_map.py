""""My own implementation of the map built-in function"""


def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable. None if the iterable can not be used by the function.
    """
    if not callable(function_to_apply):
        raise TypeError("1st argument should be callable")
    if not hasattr(iterable, '__iter__'):
        raise TypeError("2nd argument should be an iterable")
    for elem in iterable:
        yield function_to_apply(elem)


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]

    # Expected: <generator object ft_map at 0x7f709c777d00>
    print(ft_map(lambda dum: dum + 1, x))
    # Expected: [2, 4]
    print(list(ft_map(lambda dum: dum + 1, x)))
    # Expected: [1, 4, 9, 16, 25]
    print(list(ft_map(lambda x: x ** 2, x)))
    # Expected: Error
    print(ft_map(function_to_apply=None, iterable=x))
    # Expected: Error
    list(ft_map(function_to_apply=None, iterable=x))
