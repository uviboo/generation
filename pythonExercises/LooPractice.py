##CICLOS FOR##

#1.Escribe un programa que imprima los números del 1 al 10 utilizando un bucle for.
for number in range(0, 10):
  print (number+1)

#2.Calcula la suma de los primeros 10 números naturales utilizando un bucle for.
for number in range(10):
 result = sum(range(1, number+2))
 print(result)

#3.Imprime los números pares del 1 al 20 utilizando un bucle for y una sentencia if.
for number in range(1, 20+1):
  if number % 2 == 0:
      print(number)

#4.Escribe un programa que muestre la tabla de multiplicar de un número ingresado por el usuario utilizando un bucle for.
num = int(input("Ingrese un número: "))
for tabla in range(1, 11):
    resultado = num * tabla
    print(f"{num} x {tabla} = {resultado}")
#5.Dada una lista de números, calcula la suma de todos los elementos utilizando un bucle for.
list = [1, 2, 3, 4, 5]
tsum = 0
for number in list:
    tsum += number
print("La suma de los elementos es:", tsum)
  
##CICLOS WHILE##

#1.Crea un programa que cuente hacia atrás desde 10 hasta 1 utilizando un bucle while.
counter = 10
while counter >=1:
  print(counter)
  counter -=1

#2.Escribe un programa que sume números ingresados por el usuario hasta que se ingrese un número negativo utilizando un bucle while.
tsum = 0
while True:
  num = float(input("¡Suma los números que quieras! (puedes parar con un número negativo): "))
  if num < 0:
    break  
  else:
    tsum += num
print("La suma total es:", tsum)

#3.Implementa un juego de adivinanza en el que el usuario debe adivinar un número secreto. Utiliza un bucle while para permitir múltiples intentos.
import random

secret_num = random.randint(1, 20)
intentos = 0
print("¡Bienvenido al juego de adivinanzas!:D")
print("Intenta adivinar el número secreto entre 1 y 20.")
while True:
    intento = int(input("Ingrese un número: "))
    intentos += 1
    if intento == secret_num:
        print(f"¡Yay! Has adivinado el número secreto en {intentos} intentos.")
        break
    elif intento < secret_num:
        print("El número secreto es mayor. Intenta de nuevo:(.")
    else:
        print("El número secreto es menor. Intenta de nuevo:(.")

#4.Calcula el factorial de un número ingresado por el usuario utilizando un bucle while
num = int(input("Ingrese un número para calcular su factorial: "))
factorial = 1
counter = num
if num < 0:
    print("No puedo calcular eso :(.")
else:
    print(f"Procesando la factorial~ {num}:")
while counter > 0:
    factorial *= counter
    print(f"{counter}! = {factorial}")
    counter -= 1

print(f"\nEl factorial de {num} es: {factorial}")

#5.Crea un programa que genere la secuencia de Fibonacci hasta un número dado utilizando un bucle while.
limit = int(input("Ingrese el número límite para la secuencia de Fibonacci: "))
fibonacci = [0, 1]
while fibonacci[-1] + fibonacci[-2] <= limit:
    sgte_num = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(sgte_num)

print("Secuencia de Fibonacci hasta", limit, ":", fibonacci)

##SENTENCIAS IF##

#1.Escribe un programa que determine si un número ingresado por el usuario es positivo, negativo o cero utilizando sentencias if.
num = float(input("Ingrese un número: "))
if num > 0:
  print("Tu número es positivo.")
elif num < 0:
  print("Tu número es negativo.")
else:
  print("Tu número es cero.")

#2.Crea un programa que verifique si un número es par o impar utilizando una sentencia if.
num = int(input("Ingrese un número: "))
if num % 2 == 0:
      print(f"El número {num} es par.")
else:
      print(f"El número {num} es impar.")

#3.Implementa un programa que determine si un año ingresado por el usuario es bisiesto o no utilizando sentencias if.
year = int(input("Ingrese un año: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
      print(f"El año {year} es bisiesto.")
else:
      print(f"El año {year} no es bisiesto.")

#4.Solicita al usuario ingresar dos números y determina cuál de ellos es mayor utilizando sentencias if.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num1 > num2:
      print(f"{num1} es mayor que {num2}.")
elif num2 > num1:
      print(f"{num2} es mayor que {num1}.")
else:
      print("Los dos números son iguales.")

#5.Escribe un programa que determine si una contraseña ingresada por el usuario es válida (por ejemplo, debe tener al menos 8 caracteres y contener al menos una letra mayúscula y un número) utilizando sentencias if.
while True:
  contra = input("Ingrese una contraseña, debe contener al menos 8 caracteres, una mayúscula y un número: ")
  long = len(contra) >= 8
  mayus = any(c.isupper() for c in contra)
  num = any(c.isdigit() for c in contra)
  if long and mayus and num:
      print("¡Contraseña válida!")
      break
  else:
      print("Contraseña inválida. ¡Asegúrese de seguir las instrucciones!")


  
##DICCIONARIO##

#randint significa "entero aleatorio" y es una función proporcionada por el módulo aleatorio en Python. El módulo aleatorio ofrece varias funciones para generar números aleatorios. Específicamente, randint se utiliza para generar un número entero aleatorio dentro de un rango específico.#

#'len' es una función en Python que devuelve la longitud (número de caracteres) de la cadena de texto proporcionada, en este caso, la variable#

#any(x.is upper() verificará si alguna de las letras de la cadena x es una letra mayúscula.#

#any(x.isdigit() verificará si alguna de las letras de la cadena x es un dígito.#

#Un año bisiesto es divisible por 4, pero no por 100, a menos que también sea divisible por 400.#
  
#La sucesión de Fibonacci es una serie matemática infinita de números naturales que comienza con 0 y 1. Cada número en la secuencia (a partir del tercer número) es la suma de los dos números anteriores. La fórmula matemática que define la sucesión de Fibonacci es:F(n)=F(n−1)+F(n−2)#
