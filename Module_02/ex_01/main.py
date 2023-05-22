""""The goal is to learn to manipulate *args and **kwargs"""


def what_are_the_vars(*args, **kwargs):
    """Sets attrbutes of Objectc instance based on *args and **kwargs 

    Returns:
        None if there is an error, an instance of class ObjectC otherwise
    """
    my_object = ObjectC()
    for key, value in kwargs.items():
        setattr(my_object, key, value)
    for index, arg_value in enumerate(args):
        attr_name = f"var_{index}"
        if hasattr(my_object, attr_name):
            return None
        setattr(my_object, attr_name, arg_value)
    return my_object


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    """Prints all attribute from our Object instance

    Args:
        obj (Object instance)
    """
    if obj is None:
        print("ERROR")
        print("==== end ====")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print(f"{attr}: {value}")
    print("==== end ====")


if __name__ == "__main__":
    # Some simple tests to see the behavior
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)
    obj = what_are_the_vars(lambda x: x, function=what_are_the_vars)
    doom_printer(obj)
    obj = what_are_the_vars(3, var_0=2)
    doom_printer(obj)
