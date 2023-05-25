import numpy as np


class NumPyCreator:

    def _handle_data_type(self, data, dtype):
        if not isinstance(data, dtype):
            return None
        return np.array(data)

    def from_list(self, lst):
        return self._handle_data_type(lst, list)

    def from_tuple(self, tpl):
        return self._handle_data_type(tpl, tuple)

    @staticmethod
    def from_iterable(itr):
        return None

    @staticmethod
    def from_shape(shape, value):
        return None

    @staticmethod
    def random(shape):
        return None

    @staticmethod
    def identity(n, dtype=None):
        return None


if __name__ == "__main__":
    npc = NumPyCreator()
    print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
    print(npc.from_list(((1, 2), (3, 4))))
    print(npc.from_list([[1, 2, 3], ['a', 'b', 'c'], [6, 4, 7]]))
