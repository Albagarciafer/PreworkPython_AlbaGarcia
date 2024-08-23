#Ejercicios nivel básico

#1. Crea una función para verificar si un número es par o impar y devuelva “El número es par” o “El número es impar” según corresponda.

def es_par(numero):
    return numero % 2 == 0

num = int(input("Ingresa un número: "))

if es_par(num):
    print("El número es par.")
else:
    print("El número es impar.")

#2. Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado.

def factorial(numero): 
  resultado = 1 
  for i in range(1, numero+1): 
      resultado *= i 
  return resultado 

num = int(input("Ingresa un número: ")) 
print("El factorial de", num, "es:", factorial(num))

#3. Crea una función a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado total de dígitos.
def contar_digitos(numero):
     return len(str(numero)) 
num = int(input("Ingresa un número: ")) 
print("La cantidad de dígitos es:", contar_digitos(num))

#4. Dada una lista de números, crea una función que devuelva el número máximo de la lista.
def encontrar_maximo(lista): 
    maximo = lista[0] 
    for numero in lista: 
         if numero > maximo: 
            maximo = numero 
    return maximo 

numeros = [5, 12, 3, 8, 9] 
print("El número máximo es:", encontrar_maximo(numeros))

#5. Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado.
def sumar_digitos(numero): 
    suma = 0 
    while numero > 0: 
        suma += numero % 10 
        numero //= 10
    return suma 

num = int(input("Ingresa un número: ")) 
print("La suma de los dígitos es:", sumar_digitos(num))

#6. Dados dos números, crea una función para encontrar el mínimo común múltiplo (MCM) de los dos números, que se les pasarán como argumento a la función, y devuelva el MCM.

def mcm(a, b): 
    if a == 0 or b == 0: 
        return 0 
    else: 
        maximo = max(a, b) 
        while True: 
            if maximo % a == 0 and maximo % b == 0: 
                return maximo 
            maximo += 1 
num1 = int(input("Ingrese el primer número: ")) 
num2 = int(input("Ingrese el segundo número: ")) 
print("El MCM es:", mcm(num1, num2))

#7. Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo.

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

print("El área del triángulo es:", calcular_area_triangulo(base, altura))

#8. Crea una función que, dado un número, verifique si un número es positivo,negativo o cero.
def verificar_signo(num): 
    if num > 0: 
        return "positivo" 
    elif num < 0: 
        return "negativo"
    else: 
        return "cero" 
num = float(input("Ingresa un número: ")) 
print("El número es:",verificar_signo(num))

#9. Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra.
def contar_letras(palabra): 
    contador = 0 
    for letra in palabra: 
        if letra.isalpha(): 
            contador += 1 
    return contador 
palabra = input("Ingresa una palabra: ") 
print("La cantidadde letras es:", contar_letras(palabra))

#10. Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto.
def valor_absoluto(lista): 
    for i in range(len(lista)): 
        lista[i] = abs(lista[i]) 
    return lista 
numeros = [5, -12, 3, -8, 9] 
print("Lista con valores absolutos:", valor_absoluto(numeros))

#11. Crea una función que, dado un número, verifique si un número es primo.
def es_primo(numero): 
    if numero <= 1: 
        return False 
    for i in range(2, numero): 
        if numero % i == 0: 
            return False 
        return True 
num = int(input("Ingresa un número: ")) 
if es_primo(num):
    print("Es un número primo.")
else:
    print("No es un número primo.")

#12. Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números.
def mcd(a, b): 
    while b: 
        a, b = b, a % b 
    return a 
num1 = int(input("Ingresa el primer número: ")) 
num2 = int(input("Ingresa el segundo número: ")) 
print("El MCD es:", mcd(num1, num2))

#Ejercicios nivel medio 
#1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci.
def fibonacci(n):
    a, b = 0, 1  
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b  

num = int(input("Ingresa la cantidad de números de la serie de Fibonacci a imprimir: "))
fibonacci(num)

#2. Ejercicio: Define una función que tome un número y retorne una lista de sus divisores.
def encontrar_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

num = int(input("Ingresa un número para encontrar sus divisores: "))
print("Los divisores de", num, "son:", encontrar_divisores(num))

#3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.
def elementos_unicos(lista):
    lista_unicos = list(set(lista))
    return lista_unicos

entrada = input("Ingresa los elementos de la lista separados por espacios: ")
lista = list(map(int, entrada.split()))
print("Lista con elementos únicos:", elementos_unicos(lista))

#4. Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos.
def suma_digitos(numero):
    suma = 0
    numero = abs(numero)
    for digito in str(numero):
        suma += int(digito)
    return suma

num = int(input("Ingresa un número: "))
print("La suma de los dígitos es:", suma_digitos(num))

#5. Ejercicio: Define una función que tome una cadena cuente el número de vocales en la cadena.
def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    contador = 0
    
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador

texto = input("Ingresa una cadena de texto: ")
print("El número de vocales en la cadena es:", contar_vocales(texto))

#6. Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.
def primeros_n_elementos(lista, n):
    return lista[:n]
entrada = input("Ingresa los elementos de la lista separados por espacios: ")
lista = list(map(int, entrada.split()))

n = int(input("Ingresa la cantidad de elementos a retornar: "))
print("Los primeros", n, "elementos de la lista son:", primeros_n_elementos(lista, n))

#7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.
def contar_letras(cadena):
    mayusculas = 0
    minusculas = 0
    
    for caracter in cadena:
        if caracter.isalpha():  
            if caracter.isupper():  
                mayusculas += 1
            elif caracter.islower():  
                minusculas += 1
    return {'mayusculas': mayusculas, 'minusculas': minusculas}

texto = input("Ingresa una cadena de texto: ")

resultado = contar_letras(texto)
print("Cantidad de letras mayúsculas:", resultado['mayusculas'])
print("Cantidad de letras minúsculas:", resultado['minusculas'])

#8. Ejercicio: Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
def es_numero_perfecto(numero):
    if numero <= 1:
        return False  
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    return suma_divisores == numero

num = int(input("Ingresa un número: "))
if es_numero_perfecto(num):
    print(f"{num} es un número perfecto.")
else:
    print(f"{num} no es un número perfecto.")

#9. Ejercicio: Define una función que reciba un número y retorne su representación en binario.
def convertir_a_binario(numero):
    return bin(numero)[2:]

num = int(input("Ingresa un número entero: "))
print("La representación en binario es:", convertir_a_binario(num))

#10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).
def interseccion_listas(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    interseccion = conjunto1 & conjunto2
    return list(interseccion)

entrada1 = input("Ingresa los elementos de la primera lista separados por espacios: ")
entrada2 = input("Ingresa los elementos de la segunda lista separados por espacios: ")

lista1 = list(map(int, entrada1.split()))
lista2 = list(map(int, entrada2.split()))

print("La intersección de las dos listas es:", interseccion_listas(lista1, lista2))

#11. Ejercicio: Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
def es_palindromo(cadena):
    cadena_limpia = ''.join(cadena.split()).lower()
    return cadena_limpia == cadena_limpia[::-1]

texto = input("Ingresa una cadena: ")
if es_palindromo(texto):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")

#12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”.
def fizz_buzz():
    for numero in range(1, 51):
        if numero % 3 == 0 and numero % 5 == 0:
            print("FizzBuzz")
        elif numero % 3 == 0:
            print("Fizz")
        elif numero % 5 == 0:
            print("Buzz")
        else:
            print(numero)
fizz_buzz()

#13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en orden ascendente.
def ordenar_lista(lista):
    return sorted(lista)

entrada = input("Ingresa los elementos de la lista separados por espacios: ")

lista = list(map(int, entrada.split()))
print("La lista ordenada es:", ordenar_lista(lista))

#14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.
def palabras_mas_largas(palabras, n):
    return [palabra for palabra in palabras if len(palabra) > n]

entrada_palabras = input("Ingresa una lista de palabras separadas por espacios: ")
n = int(input("Ingresa el número de caracteres: "))

lista_palabras = entrada_palabras.split()
resultado = palabras_mas_largas(lista_palabras, n)
print("Las palabras que son más largas que", n, "son:", resultado)

#15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci.
def serie_fibonacci(n):
    fibonacci = []
    a, b = 0, 1
    
    for _ in range(n):
        fibonacci.append(a)
        a, b = b, a + b
    return fibonacci

n = int(input("Ingresa el número de términos de la serie de Fibonacci: "))
resultado = serie_fibonacci(n)
print("La serie de Fibonacci hasta el", n, "es:", resultado)

#16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista.
def encontrar_maximo(lista):
    return max(lista)

entrada = input("Ingresa una lista de números separados por espacios: ")
lista_numeros = list(map(float, entrada.split()))
resultado = encontrar_maximo(lista_numeros)
print("El número más grande en la lista es:", resultado)

#17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
def suma_digitos_al_cubo(numero):
    numero = abs(numero)
    suma_digitos = sum(int(digito) for digito in str(numero))
    return suma_digitos ** 3

numero = int(input("Ingresa un número: "))
resultado = suma_digitos_al_cubo(numero)
print("La suma de los dígitos al cubo es:", resultado)

#18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.
def segundo_mas_grande(lista):
    lista_unica = list(set(lista))
    if len(lista_unica) < 2:
        raise ValueError("La lista debe contener al menos dos números únicos.")
    lista_unica.sort(reverse=True)
    return lista_unica[1]

entrada = input("Ingresa una lista de números separados por espacios: ")
lista_numeros = list(map(float, entrada.split()))
resultado = segundo_mas_grande(lista_numeros)
print("El segundo número más grande en la lista es:", resultado)

#19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.
def tienen_elemento_comun(lista1, lista2):
    return bool(set(lista1) & set(lista2))

entrada1 = input("Ingresa los elementos de la primera lista separados por espacios: ")
entrada2 = input("Ingresa los elementos de la segunda lista separados por espacios: ")
lista1 = entrada1.split()
lista2 = entrada2.split()

resultado = tienen_elemento_comun(lista1, lista2)
print("Las listas tienen al menos un miembro en común:", resultado)

#20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.
def invertir_lista(lista):
    return lista[::-1]

entrada = input("Ingresa los elementos de la lista separados por espacios: ")
lista_original = entrada.split()

lista_invertida = invertir_lista(lista_original)
print("La lista en orden inverso es:", lista_invertida)

#21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.
def contar_digitos_y_letras(cadena):
    conteo_letras = 0
    conteo_digitos = 0

    for caracter in cadena:
        if caracter.isalpha():  
            conteo_letras += 1
        elif caracter.isdigit():  
            conteo_digitos += 1
    return conteo_letras, conteo_digitos

cadena = input("Ingresa una cadena de texto: ")
letras, digitos = contar_digitos_y_letras(cadena)
print("Número de letras en la cadena:", letras)
print("Número de dígitos en la cadena:", digitos)

#22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números
def suma_acumulada(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

entrada = input("Ingresa una lista de números separados por espacios: ")
lista_numeros = list(map(float, entrada.split()))
resultado = suma_acumulada(lista_numeros)
print("La suma acumulada de los números es:", resultado)

#23. Ejercicio: Define una función que encuentre el elemento más común en una lista.
from collections import Counter
def elemento_mas_comun(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía.")
    
    conteo = Counter(lista)
    elemento_comun, frecuencia = conteo.most_common(1)[0]
    return elemento_comun

entrada = input("Ingresa los elementos de la lista separados por espacios: ")
lista_elementos = entrada.split()
resultado = elemento_mas_comun(lista_elementos)
print("El elemento más común en la lista es:", resultado)

#24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.
def tabla_multiplicar(numero):
    tabla = {}
    for i in range(1, 11):  # Iterar del 1 al 10
        tabla[i] = numero * i
    return tabla

num = int(input("Ingresa un número para generar su tabla de multiplicar: "))
resultado = tabla_multiplicar(num)
print("La tabla de multiplicar del número", num, "es:")
for clave, valor in resultado.items():
    print(f"{num} x {clave} = {valor}")

#25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.
def contar_caracteres(cadena):
    conteo = {}
    
    for caracter in cadena:
        if caracter in conteo:
            conteo[caracter] += 1
        else:
            conteo[caracter] = 1
    return conteo

cadena = input("Ingresa una cadena de texto: ")
resultado = contar_caracteres(cadena)
print("Cantidad de apariciones de cada carácter en la cadena:")
for caracter, cantidad in resultado.items():
    print(f"'{caracter}': {cantidad}")

#26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
def diferencia_listas(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    diferencia = set1.symmetric_difference(set2)
    return list(diferencia)

entrada1 = input("Ingresa los elementos de la primera lista separados por espacios: ")
entrada2 = input("Ingresa los elementos de la segunda lista separados por espacios: ")
lista1 = entrada1.split()
lista2 = entrada2.split()
resultado = diferencia_listas(lista1, lista2)
print("Elementos que no están en ambas listas:", resultado)

#27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados.
def eliminar_duplicados(lista):
    conjunto = set(lista)
    lista_sin_duplicados = list(conjunto)
    return lista_sin_duplicados

entrada = input("Ingresa los elementos de la lista separados por espacios: ")
lista_elementos = entrada.split()
resultado = eliminar_duplicados(lista_elementos)
print("Lista sin duplicados:", resultado)

#28. Ejercicio: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.
def suma_cuadrados_pares(n):
    if n < 0:
        raise ValueError("El número debe ser entero positivo.")
    
    suma = 0
    for i in range(2, n + 1, 2):  
        suma += i ** 2  
    return suma

num = int(input("Ingresa un número entero positivo: "))
resultado = suma_cuadrados_pares(num)
print("La suma de los cuadrados de los números pares menores o iguales a", num, "es:", resultado)

#29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista.
def calcular_promedio(lista):
    if not lista:
        return 0  
    suma = sum(lista)  
    cantidad = len(lista)  
    promedio = suma / cantidad  
    return promedio

entrada = input("Ingresa los números separados por espacios: ")
numeros = list(map(float, entrada.split()))
resultado = calcular_promedio(numeros)
print("El promedio de los números en la lista es:", resultado)

#30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.
def cadena_mas_larga(lista_cadenas):
    if not lista_cadenas:
        return ""
    cadena_larga = lista_cadenas[0]
    for cadena in lista_cadenas:
        if len(cadena) > len(cadena_larga):
            cadena_larga = cadena
    return cadena_larga

entrada = input("Ingresa las cadenas separadas por comas: ")
cadenas = [cadena.strip() for cadena in entrada.split(',')]
resultado = cadena_mas_larga(cadenas)
print("La cadena más larga es:", resultado)

#31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.
def es_primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def primeros_n_primos(n):
    primos = []
    candidato = 2 
    while len(primos) < n:
        if es_primo(candidato):
            primos.append(candidato)
        candidato += 1
    return primos

num = int(input("Ingresa la cantidad de números primos que deseas: "))
resultado = primeros_n_primos(num)
print("Los primeros", num, "números primos son:", resultado)

#32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.
def invertir_palabras(cadena):
    palabras = cadena.split()
    palabras_invertidas = palabras[::-1]
    resultado = ' '.join(palabras_invertidas)  
    return resultado

texto = input("Ingresa una cadena de texto: ")
resultado = invertir_palabras(texto)
print("La cadena con las palabras en orden inverso es:", resultado)

#33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.
def ordenar_por_ultimo_elemento(lista_tuplas):
    lista_ordenada = sorted(lista_tuplas, key=lambda tupla: tupla[-1])
    return lista_ordenada

entrada = input("Ingresa una lista de tuplas (por ejemplo, [(1, 3), (2, 2), (3, 1)]): ")
import ast
lista_tuplas = ast.literal_eval(entrada)

#34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.
def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    conteo = 0

    for caracter in cadena:
        if caracter in vocales:
            conteo += 1
    return conteo

texto = input("Ingresa una cadena de texto: ")
resultado = contar_vocales(texto)
print("La cantidad de letras vocales en la cadena es:", resultado)

#35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False
import math

def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

num = int(input("Ingresa un número entero: "))
resultado = es_primo(num)
if resultado:
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")