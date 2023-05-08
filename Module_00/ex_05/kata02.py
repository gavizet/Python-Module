kata = (2019, 9, 25, 3, 30)

def kata_02(my_kata):
    day     = my_kata[1]
    month   = my_kata[2]
    year    = my_kata[0]
    hour    = my_kata[3]
    minute  = my_kata[4]
    message = f"{day:02}/{month:02}/{year:04} {hour:02}:{minute:02}"
    print(message)

if __name__ == "__main__":
    kata_02(kata)