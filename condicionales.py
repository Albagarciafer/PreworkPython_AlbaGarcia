#1. Ejercicio: Dado un número, imprime si es positivo o negativo.
numero = 3
def determinar_signo(numero): 
  if numero > 0:
      print(f'El número {numero} es positivo')
  elif numero < 0: 
      print(f'El número {numero} es negativo')
  else:
      print(f'El número es cero')
determinar_signo(numero)


#2. Ejercicio: Dado un número, imprime si es par o impar.
def determinar_par(numero): 
    if numero % 2 == 0:
      print('El número es par')
    else:
      print('El número es impar')
determinar_par(numero)


#3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
a = 3
b = 7
c = 5

def encontrar_mayor(a, b, c): 
    if a > b and a > c:
      return a
    elif b > c and b > a:
      return b
    else:
      return c 
mayor = encontrar_mayor(a, b, c) 
print(mayor)