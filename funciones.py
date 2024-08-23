#1. Ejercicio: Define una función que tome dos números y retorne su suma.
def sumar_dos_numeros(numero1, numero2):
  suma = numero1 + numero2
  return suma

numero1 = 2
numero2 = 5
resultado = sumar_dos_numeros(numero1, numero2) 
print(resultado)

#2. Ejercicio: Define una función que tome un número y retorne su factorial.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(0))
print(factorial(5))

#3. Ejercicio: Define una función que tome un número y determine si es primo.
def es_primo(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

print(es_primo(2))
print(es_primo(4))
print(es_primo(11))

#4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos.
def suma_lista(numeros):
    suma = sum(numeros)
    return suma

lista_de_numeros = [1, 2, 3, 4, 5]
resultado = suma_lista(lista_de_numeros)
print("La suma de la lista es:", resultado)

#5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa.
def reversa_cadena(cadena):
    return cadena[::-1]

texto = "Hola, mundo!"
resultado = reversa_cadena(texto)
print("La cadena en reversa es:", resultado)
