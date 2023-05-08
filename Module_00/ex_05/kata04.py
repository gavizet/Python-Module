kata = (1234567890, 0, -12, 45.45675, 12.123)

def kata_04(my_kata):
    message = (
        f"module_{my_kata[0]:02d}, "
        f"ex_{my_kata[1]:02d} : "
        f"{my_kata[2]:.2f}, "
        f"{my_kata[3]:.2e}, "
        f"{my_kata[4]:.2e}"
    )
    print(message)

if __name__ == "__main__":
    kata_04(kata)