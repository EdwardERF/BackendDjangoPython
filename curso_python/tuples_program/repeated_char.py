def first_not_repeating_char(char_sequence):
    seen_letters = {}

    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

    final_letters = []
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letters.append( (key, value[0]) )

    not_repeated_letters = sorted(final_letters, key = lambda value: value[1])
    # (traduccion: ordename final_letters de acuerdo a key, que es el segundo valor (0, 1)
    # de final_letters)

    # lamba value: value[1]
    # es lo mismo que la siguiente función

    # def sort_order(value):
    #     return value[1]
    
    # es una abreviación de la misma función
    # por tanto se podría cambiar a key = sort_order(value)

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'


if __name__ == "__main__":
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten')
    else:
        print(f'El primer caracter no repetido es: {result}')


