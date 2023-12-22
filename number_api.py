import json
import requests

def main():
    pass

    first_try = True

    while True:
        if first_try:
            num = input("Ingrese un número: ")
            first_try = False
        else:
            num = input("Ingrese un número (o ingrese 0 para salir): ")

        if num == '0':
            print("¡Muchas gracias por participar en la trivia!")
            break

        try:
            num = int(num)
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        get_and_print_trivia(num)

def get_and_print_trivia(num):
    response = requests.get(f"http://numbersapi.com/{num}?json")

    if response.status_code == 200:
        trivia = json.loads(response.content)
        print(trivia["text"])
    else:
        print(f"Error al obtener la trivia para el número {num}. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()


#Response.status_code: Evita que se caiga el programa al haber errores. En este caso 200code=OK (https://http.cat/).
#json.loads: Convierte el contenido de la respuesta en un objeto de Python.
#La instrucción `pass` es una operación nula, lo que significa que no hace nada. Sirve como marcador de posición cuando se requiere sintácticamente algún código, pero no deseas ejecutar ninguna instrucción, en este caso cambié el print original porque no lo necesitaba.
#Me gustaría agregar otra api que tradujese la trivia a español.
