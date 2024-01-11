while True:
  UserNum = input("Ingrese tres números separados por comas o escriba 'x' para salir: ")

  if UserNum.lower() == 'x':
      break  

  try:
      numeros = [int(numero) for numero in UserNum.split(',')]

      if len(numeros) != 3:
          print("Por favor, ingrese exactamente tres números.")
      else:
          mayor = max(numeros)
          menor = min(numeros)
          centro = sum(numeros) - mayor - menor

          print("Números ordenados de mayor a menor:", sorted(numeros, reverse=True))
        
          print("Números ordenados de menor a mayor:", sorted(numeros))

          if numeros[0] == numeros[1] == numeros[2]:
              print("Los números son iguales.")
          else:
              print("Número mayor:", mayor, "Número del centro:", centro, "Número menor:", menor)

  except ValueError:
      print("Valor inválido, intente nuevamente.")
