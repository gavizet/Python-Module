kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

def kata_01(my_kata):
    message = ''
    for key, value in my_kata.items():
        print(f"{key} was created by {value}")

if __name__ == "__main__":
    kata_01(kata)