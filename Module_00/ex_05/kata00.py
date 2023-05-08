kata = ("",42,21)

def kata_00(my_kata):
    length = len(my_kata)
    message = f"The {length} numbers are: {', '.join(map(str, my_kata))}"
    print(message)

if __name__ == "__main__":
    kata_00(kata)