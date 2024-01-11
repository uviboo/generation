##Takes two input numbers, then adds them together and prints the result
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
def add(num1, num2):
  result = num1 + num2
  return  result
print (add(num1, num2))

##Take two numbers and subtract the second from the first number.
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
def rest(num1, num2):
  result = num1 - num2
  return  result
print (rest(num1, num2))

##Take two numbers and divide the first number by the second number.

num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese otro número: "))
def division(num1, num2):
  result = num1 / num2
  return  result
print (division(num1, num2))

##Take two numbers and perform a modulus operation.
num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese otro número: "))
def mod(num1, num2):
  result = num1 % num2
  return  result
print (mod(num1, num2))

##Allow users to choose which operation they want to perform on two numbers.
operation = input("Elige una operación (+, -, /, %): ")
num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese otro número: "))
if operation == '+':
    print(f"El resultado de la operación es: {num1 + num2} ")
elif operation == '-':
    print(f" El resultado de la operación es : {num1 - num2} ")
elif operation == '/':
    print(f" El resultado de la operación es: {num1 / num2} ")
elif operation == '%':
    print(f" El resultado de la operación es: {num1 % num2} ")
else:
    print("Operación inválida")

##Take 3 numbers and add them together.
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
num3 = int(input("Ingrese otro número: "))
resultado = num1 + num2 + num3
print(f"La suma de los tres números es {resultado}")

##Allow users to mix operations with 3 numbers or more e.g. 2 + 4 - 3, 4 *5 + 1 / 3
expression = input("Ingresa un cálculo de 3 o más números: ")
try:
  result = eval(expression)
  print(f"El resultado de tu cálculo es: {result}")
except NameError:
    print("Error: La expresión ingresada no es válida. Por favor ingresa una expresión matemática válida.")
#La función eval() en Python es una función incorporada que se utiliza para evaluar expresiones o cadenas de texto que contienen código Python válido. Toma una cadena de texto como argumento y la interpreta como código Python, ejecutando ese código y devolviendo el resultado.
#En este caso, la función eval() se utiliza para evaluar la expresión ingresada

