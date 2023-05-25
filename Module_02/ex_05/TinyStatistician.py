"""Initiation to very basic statistic notions
We don't have to protect our program against non-valid inputs"""


class TinyStatistician:
    """ Performs basic statistical calculations """

    def __init__(self):
        pass

    def mean(self, lst):
        """ Calculates the mean of a list of numbers.

        Args:
            lst: list of numbers

        Returns:
            The mean value of the elements in the list. If the input list is empty, returns None
        """
        if not lst:
            return None
        result = 0
        elem_num = len(lst)
        for elem in lst:
            result += elem
        return result / elem_num

    def median(self, lst):
        """ Calculates the median of a list of numbers.

        Args:
            lst: list of numbers

        Returns:
            The median value of the elements in the list. If the input list is empty, returns None
        """
        if not lst:
            return None
        lst.sort()
        mid_elem = len(lst) // 2
        result = (lst[mid_elem] + lst[-mid_elem-1]) / 2
        return result

    def quartiles(self, lst):
        """ Calculates the 1st and 3rd Quartiles of a list of numbers.

        Args:
            lst: list of numbers

        Returns:
            The quartiles value of the elements in the list.
            If the input list is empty, returns None
        """
        if not lst:
            return None
        lst.sort()
        middle = len(lst) // 2
        quartile1 = self.median(lst[:middle])
        quartile3 = self.median(lst[-middle:])
        result = [quartile1, quartile3]
        return result

    def var(self, lst):
        """ Calculates the variance of a list of numbers.

        Args:
            lst: list of numbers

        Returns:
            The variance value of the elements in the list.
            If the input list is empty, returns None
        """
        if not lst:
            return None
        variance = 0
        mean = self.mean(lst)
        for elem in lst:
            variance += (elem - mean) ** 2
        return variance / len(lst)

    def std(self, lst):
        """ Calculates the standard deviation of a list of numbers.

        Args:
            lst: list of numbers

        Returns:
            The standard deviation value of the elements in the list.
            If the input list is empty, returns None
        """
        if not lst:
            return None
        return self.var(lst) ** 0.5


if __name__ == "__main__":
    stats = TinyStatistician()
    x = [1, 42, 300, 10, 59]

    # Expected result: 82.4
    print("==== MEAN ====")
    print("Expected: 82.4")
    print(f"Result: {stats.mean(x)}")

    # Expected result: 42.0
    print("==== MEDIAN ====")
    print("Expected: 42.0")
    print(f"Result: {stats.median(x)}")

    # Expected result: [5.5, 179.5]
    print("==== QUARTILES ====")
    print("Expected: [5.5, 179.5]")
    print(f"Result: {stats.quartiles(x)}")

    # Expected result: 12279.439999999999
    print("==== VAR ====")
    print("Expected: 12279.439999999999")
    print(f"Result: {stats.var(x)}")

    # Expected result: 110.81263465868862
    print("==== STD ====")
    print("Expected: 110.81263465868862")
    print(f"Result: {stats.std(x)}")
