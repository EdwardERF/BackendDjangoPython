import random

def main():
    random_number = random.randint(1, 100)
    numero_elegido = int(input('Elige un numero del 1 al 100: '))

    while numero_elegido != random_number:
        if numero_elegido < random_number:
            print('Busca un numero mayor')
            numero_elegido = int(input('Elige otro numero: '))
        elif numero_elegido > random_number:
            print('Busca un numero menor')
            numero_elegido = int(input('Elige otro numero: '))

    print('Ganaste!')


if __name__ == "__main__":
    main()