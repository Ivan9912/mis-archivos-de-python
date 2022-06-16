#Métodos de operaciones
def sumar(par1, par2):
    num1 = int(par1)
    num2 = int(par2)

    suma = num1 + num2
    return suma

def restar(par1, par2):
    num1 = int(par1)
    num2 = int(par2)

    resta = num1 - num2
    return resta

def multiplicar(par1, par2):
    num1 = int(par1)
    num2 = int(par2)

    multiplicacion = num1 * num2
    return multiplicacion

def dividir(par1, par2):
    num1 = float(par1)
    num2 = float(par2)

    multiplicacion = num1 / num2
    return multiplicacion

#Método de elección de operación a realizar
def menu():
    opcion = ["sumar", "restar", "multiplicar", "dividir"]

    opciones = opcion[0] + ", " + opcion[1] + ", " + opcion[2] + ", " + opcion[3]
    elegir_opcion = input("Elige una opción (" + opciones + "): ")

    if elegir_opcion not in opcion:
        print("Esa opción no existe.")
    else:
        if elegir_opcion == opcion[0]:
            num1 = input("Escribe un primer número: ")
            num2 = input("Escribe un segundo número: ")

            print("El resultado es: ")
            print(sumar(num1, num2))

        elif elegir_opcion == opcion[1]:
            num1 = input("Escribe un primer número: ")
            num2 = input("Escribe un segundo número: ")

            print("El resultado es: ")
            print(restar(num1, num2))

        elif elegir_opcion == opcion[2]:
            num1 = input("Escribe un primer número: ")
            num2 = input("Escribe un segundo número: ")

            print("El resultado es: ")
            print(multiplicar(num1, num2))

        elif elegir_opcion == opcion[3]:
            num1 = input("Escribe un primer número: ")
            num2 = input("Escribe un segundo número: ")

            print("El resultado es: ")
            print(dividir(num1, num2))

menu()