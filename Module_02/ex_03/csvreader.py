"""The goal of this exercise is to implement a context manager as a class."""
import os.path
import logging
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s -  %(levelname)s -  %(message)s')


class CsvReader:
    """Context manager that parses, opens and reads a CSV file"""

    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.file = None
        self.filename = filename
        self.all_lines = []
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        logging.debug("Init")

    def __enter__(self):
        logging.debug("Enter")
        if os.path.isfile(self.filename):
            self.file = open(self.filename, 'r', encoding='utf-8')
            self.all_lines = self.file.readlines()
            logging.debug("File opened")
        else:
            logging.debug("File not found")
            raise FileNotFoundError(f"'{self.filename}' not found.")
        return self.file

    def __exit__(self, exc_type, exc_instance, exc_traceback):
        logging.debug("Exit")
        if self.file is not None:
            logging.debug("File exists, closing")
            self.file.close()
        if not exc_type:
            logging.debug("no exception caught, returning True")
            return True
        print(f"Exception caught: {exc_type} - {exc_instance}")
        return None

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.

        Return:
            nested list (list(list, list, ...)) representing the data.
        """
        line_number = len(self.all_lines)
        if self.header is True:
            self.skip_top += 1
        lines_to_skip = self.skip_top + self.skip_bottom
        if line_number == 0 or line_number <= lines_to_skip:
            return []
        return all_lines[self.skip_top:-self.skip_bottom]

    def getheader(self):
        """ Retrieves the header from csv file.

        Returns:
            list: representing the data (when self.header is True).
            None: (when self.header is False).
        """
        if self.header is None:
            return None
        else:
            return self.all_lines[0]


"""
# Does not exist file
if __name__ == "__main__":
    with CsvReader('haha.csv') as file:
        data = file.getdata()
        header = file.getheader()

# Bad file
if __name__ == "__main__":
    with CsvReader('Module_02/ex_03/bad.csv') as file:
        if file is None:
            print("File is corrupted")"""

# Good file
if __name__ == "__main__":
    with CsvReader('Module_02/ex_03/good.csv', skip_top=10, skip_bottom=10) as my_file:
        data = my_file.getdata()
        # header = file.getheader()
