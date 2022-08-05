"""
Cada nuevo término en la sucesión de Fibonacci se genera sumando los dos términos anteriores. 
Al comenzar con 1 y 2, los primeros 10 términos serán:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Al considerar los términos en la sucesión de Fibonacci cuyos valores no superan los cuatro millones, 
encuentre la suma de los términos de valor par.
"""
numeros = []
total=0
for i in range(10):
    if i>=2:
        valor = numeros[i-1] + numeros[i-2]
        if valor % 2==0:
            total+=valor;
        numeros.append(valor)
    else:
        numeros.append(i)   
print(numeros) #Secuencia fibonaci
print("La suma de los números pares hasta 4.000.000 es {}".format(total))
    
        