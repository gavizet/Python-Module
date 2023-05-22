""""My own implementation of the reduce function from functools module"""


def ft_reduce(function_to_apply, iterable):
    """Reduce the function to all elements of the iterable.
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
    if len(iterable) == 0:
        raise IndexError("Can't iterate, no range on iterable")
    result = iterable[0]
    for elem in iterable[1:]:
        result = function_to_apply(result, elem)
    return result


if __name__ == "__main__":
    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
    x = [1, 2, 3, 4]
    # Expected: "Hello world"
    print(ft_reduce(lambda u, v: u + v, lst))
    # Expected: 24
    print(ft_reduce(lambda u, v: u * v, x))
    # Expected: 1
    print(ft_reduce(lambda u, v: u + v, [1]))
    # Expected: 1
    print(ft_reduce(lambda u, v: u + v, []))
    # Expected: Error
    print(ft_reduce(lambda u, v: u + v, iterable=None))
    # Expected: Error
    print(ft_reduce(function_to_apply=None, iterable=lst))
