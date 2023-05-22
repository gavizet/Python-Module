"""The goal of this exercise is to implement a context manager as a class."""


class CsvReader:
    """Context manager that parses, opens and reads a CSV file"""

    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        pass

    def __enter__(self):
        pass

    def __exit__(self):
        pass

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.

        Return:
            nested list (list(list, list, ...)) representing the data.
        """

    def getheader(self):
        """ Retrieves the header from csv file.

        Returns:
            list: representing the data (when self.header is True).
            None: (when self.header is False).
        """


# Good file
if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()

# Bad file
if __name__ == "__main__":
    with CsvReader('bad.csv') as file:
        if file is None:
            print("File is corrupted")
