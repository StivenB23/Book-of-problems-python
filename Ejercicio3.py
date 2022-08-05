"""
Los factores primos de 13195 son 5, 7, 13 y 29.

¿Cuál es el mayor factor primo del número 600851475143?
"""
import math
def divisores(numero):
    num = math.ceil(numero / 2)
    for i in range(2, num):
        if numero % i == 0:
            return i
    return numero

numero = 13195
posicion = 0
factorMayor = 0
while numero != 1:
    divisor = divisores(numero)
    numero = numero / divisor
    factorMayor = divisor
print(int(factorMayor))