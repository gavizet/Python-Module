kata = "The right format"

def kata_03(my_kata):
    message = f"{my_kata:->42}"
    print(message, end="")

if __name__ == "__main__":
    kata_03(kata)