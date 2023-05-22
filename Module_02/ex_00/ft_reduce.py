""""My own implementation of the reduce function from functools module"""


def ft_reduce(function_to_apply, iterable):
    """Reduce the function to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable. None if the iterable can not be used by the function.
    """
