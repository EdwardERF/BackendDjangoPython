def main():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Brasil' : 210147125,
        'Argentina' : 44938712,
        'Uruguay' : 3200000,
    }

    for pais in poblacion_paises.keys():
        print(f'Pais: {pais}')

    for values in poblacion_paises.values():
        print(f'Poblacion: {values}')
    
    for pais, poblacion in poblacion_paises.items():
        print(f'{pais} tiene {poblacion} habitantes')

if __name__ == "__main__":
    main()