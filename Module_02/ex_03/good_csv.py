from Module_02.ex_03.csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('Module_02/ex_03/good.csv', header=True, skip_top=0, skip_bottom=0) as my_file:
        header = my_file.getheader()
        print("===== HEADER =====")
        print(header)
        print("====== DATA ======")
        data = my_file.getdata()
        print(data)
