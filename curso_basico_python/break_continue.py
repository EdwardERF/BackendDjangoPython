def main():
    # continue para iterar sin hacer nada en determinadas condiciones
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # break en ciclo de numeros
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    # break en string
    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)

if __name__ == "__main__":
    main()