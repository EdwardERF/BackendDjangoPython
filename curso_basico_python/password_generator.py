import random


def generate_password():
    capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 's']
    symbols = ['!', '#', '$', '&', '/', '(', ')']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    characters = capitals + lowers + symbols + numbers

    password = []

    for i in range(15):
        random_character = random.choice(characters)
        password.append(random_character)

    password = ''.join(password) # Esto genera un string con el contenido de una lista.

    return password


def main():
    password = generate_password()
    print(f'Your new password is {password}')

if __name__ == "__main__":
    main()