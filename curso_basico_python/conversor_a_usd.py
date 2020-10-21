pesos = input('¿Cuántos pesos uruguayos tienes?: ')
pesos = float(pesos)
valor_dolar = 44
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print(f"Tienes {dolares} dolares")