from Module_02.ex_03.csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('haha.csv') as file:
        data = file.getdata()
        header = file.getheader()
