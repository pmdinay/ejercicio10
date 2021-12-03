"""Programa"""
import stats_data as sd
lista = []
while True:
    numeros = input('Introduce números: ')
    if numeros == "fin":
        break
    numeros = float(numeros)
    lista.append(numeros)
print(lista)

res = sd.StatsData(lista)
print("Lista números: ", res.l_data)
print("Mediana: ", res.mean)
print("Mediana: ", res.median)
print("Varianza: ", res.variance)