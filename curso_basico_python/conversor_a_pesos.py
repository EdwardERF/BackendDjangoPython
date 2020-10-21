dolares = input('Cuantos dolares tienes?: ')
dolares = float(dolares)
valor_dolar = 44
pesos = dolares * valor_dolar
pesos = round(pesos, 0)
pesos = str(pesos)
print(f'Tienes {pesos} pesos')