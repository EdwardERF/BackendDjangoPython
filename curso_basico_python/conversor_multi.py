def conversor(tipo_pesos, valor_dolar):
    dolares = input('Cuantos dolares tienes?: ')
    dolares = float(dolares)
    pesos = dolares * valor_dolar
    pesos = round(pesos, 0)
    pesos = str(pesos)
    print(f'Tienes {pesos} pesos {tipo_pesos}')

menu = """
Bienvenido al conversor de monedas 😊

1 - Pesos uruguayos
2 - Pesos colombianos
3 - Pesos argentinos

Elige una opción: """

opcion = input(menu)

if opcion == '1':
    conversor('uruguayos', 44)
elif opcion == '2':
    conversor('colombianos', 3875)
elif opcion == '3':
    conversor('argentinos', 65)
else:
    print('Ingresa una opción correcta.')