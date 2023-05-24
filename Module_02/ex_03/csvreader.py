"""The goal of this exercise is to implement a context manager as a class."""
import os.path
import logging
# Change this level to level=logging.DEBUG to see all the logging
logging.basicConfig(level=logging.ERROR,
                    format=' %(asctime)s -  %(levelname)s -  %(message)s')


class CsvReader:
    """Context manager that parses, opens and reads a CSV file"""

    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        if filename is None:
            raise ValueError("You might want to give me a file to read")
        if not isinstance(filename, str) or not isinstance(sep, str):
            raise ValueError("fileame and separator need to be strings")
        if not isinstance(header, bool):
            raise ValueError("header arg needs to be a boolean")
        if not isinstance(skip_top, int) or not isinstance(skip_bottom, int) or\
                skip_top < 0 or skip_bottom < 0:
            raise ValueError("skip_top & skip_bottom have to be positive ints")
        self.file = None
        self.filename = filename
        self.file_data = []
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        logging.debug("Init")

    def __enter__(self):
        logging.debug("Enter")
        if not os.path.isfile(self.filename):
            logging.debug("File not found")
            raise FileNotFoundError(f"'{self.filename}' not found.")
        self.file = open(self.filename, 'r', encoding='utf-8')
        logging.debug("File opened")
        for index, line in enumerate(self.file):
            line = self.parse_line(line)
            # Elem_count initialized based on 1st line (header)
            if index == 0:
                elem_count = len(line)
            # If ant future line doesn't have the same number of elements,
            # then csv file is corrupted
            if len(line) != elem_count:
                return None
            self.file_data.append(line)
        logging.debug("File parsed")
        return self

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

    def parse_line(self, line) -> list:
        """
        This function takes a string and splits it into a list of elements, removing any trailing
        newline characters and whitespace.

        Args:
          line: string that represents a line of text that needs to be parsed.
        Returns:
            A list of elements that were parsed
        """
        line = line.rstrip('\n')
        line = line.split(self.sep)
        line = [elem.strip() for elem in line]
        return line

    def getdata(self):
        """ Retrieves the file data/records from skip_top to skip bottom.

        Return:
            nested list (list(list, list, ...)) representing the data.
        """
        line_number = len(self.file_data)
        if self.header is True:
            self.skip_top += 1
        lines_to_skip = self.skip_top + self.skip_bottom
        if line_number == 0 or line_number <= lines_to_skip:
            return []
        end = line_number - self.skip_bottom
        return self.file_data[self.skip_top:end]

    def getheader(self):
        """ Retrieves the header from csv file.

        Returns:
            list: representing the data (when self.header is True).
            None: (when self.header is False).
        """
        if self.header is None:
            return None
        return self.file_data[0]
