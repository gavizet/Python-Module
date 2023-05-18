import pytest
from Module_01.ex_02.vector import Vector

VECTORS = [
    Vector(5),  # Valid int vector
    Vector((10, 16)),  # Valid range vector
    Vector(range(10, 16)),  # Valid range vector
    Vector([[0.0], [1.0], [2.0], [3.0]]),  # Valid column vector
    Vector([[0.0, 1.0, 2.0, 3.0]]),  # Valid row vector
    Vector("stupid test"),  # Error string
    Vector(-3),  # Error negative int
    Vector((10, 6)),  # Error tuple with a > b
    Vector([0.0, 1.0, 2.0, 3.0]),  # Error list of floats
    Vector([[0.0, 1.0], [2.0, 3.0]]),  # Error more than 1 float / sublist
    Vector([[]])  # Error empty sublist
]
