def first_not_repeating_char(char_sequence):
    sequence_separated = char_sequence.split('')
    return sequence_separated


if __name__ == "__main__":
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    print(result)