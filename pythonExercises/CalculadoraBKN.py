def addmultiplenumbers(numbers):
  numbers_str = numbers.split()
  numbers_list = [int(x) for x in numbers_str]
  return sum(numbers_list)

def multiplymultiplenumbers(numbers):
  numbers_str = numbers.split()
  numbers_list = [int(x) for x in numbers_str]
  result = 1
  for num in numbers_list:
      result *= num
  return result

def isiteven(num):
  return num % 2 == 0

def isitaninteger(num):
  try:
      int(num)
      return True
  except ValueError:
      return False

def freemath(expression):
  try:
      result = eval(expression)
  except NameError:
      print("Error: La expresión ingresada no es válida. Inténtelo nuevamente.")
      return None
  return result

def main():
  print("¡Ésta es mi calculadora!")

  while True:
      print("\nMenu:")
      print("1. Suma")
      print("2. Multiplicación")
      print("3. ¿Es este número par?")
      print("4. ¿Es este un número entero?")
      print("5. Operación libre")
      print("6. Salir")

      choice = input("Elige un número (1-6): ")

      if choice == '1':
          numbers = input("Ingresa números separados por un espacio: ")
          result = addmultiplenumbers(numbers)
          print("Suma:", result)
      elif choice == '2':
          numbers = input("Ingresa números separados por un espacio: ")
          result = multiplymultiplenumbers(numbers)
          print("Producto:", result)
      elif choice == '3':
          num = int(input("Ingresa un número: "))
          result = isiteven(num)
          print(f"¿Es {num} par?:", result)
      elif choice == '4':
          num = input("Ingresa un número: ")
          result = isitaninteger(num)
          print(f"¿Es {num} un entero?:", result)
      elif choice == '5':
          expression = input("Ingresa un cálculo de 3 o más números: ")
          result = freemath(expression)
          if result is not None:
              print(f"El resultado de tu cálculo es: {result}")
      elif choice == '6':
          print("¡Muchas gracias por usar mi calculadora!")
          break
      else:
          print("La opción ingresada no es válida. Inténtelo nuevamente.")

if __name__ == "__main__":
  main()
##Split:nos sirve para separar los elementos de una cadena de texto en una lista,esto puede ser a través de un espacio en blanco, una coma o cualquier otro caracter que nosotros le asignemos en (). 
