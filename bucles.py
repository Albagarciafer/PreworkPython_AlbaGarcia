#1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
numeros =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros: 
    print(numero)

#2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
i = 1
while i <= 20: 
    if i % 2 == 0: 
        print(i)
    i+=1

#3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
i = 1
suma = 0
while i <= 100:
    suma += i
    i+=1
print(f'La suma de los númros del 1 al 100 es:{suma}')

