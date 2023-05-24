from Module_02.ex_03.csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('Module_02/ex_03/bad.csv') as file:
        if file is None:
            print("File is corrupted")
