from multiprocessing.sharedctypes import Value
from inverso import *
import sys
def sumaModular():
    try:
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo numero: "))
        mod = int(input("Ingrese el modulo (Zn): "))
        while a <= 0 or b <= 0 or mod <= 0:
            print("No puedes ingresar valores negativos, vuelve a intentarlo")
            sumaModular()
        if a < mod:
            a = a % mod
        else:
            if b < mod:
                b = b % mod
        suma = a + b 
        suma = suma % mod
        return suma
    except ValueError:
        print("Debes ingresar valores numericos, vuelve a intentarlo")
        sumaModular()

def multiplicacionModular():
    try:
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo numero: "))
        mod = int(input("Ingrese el modulo (Zn): "))
        while a <= 0 or b <= 0 or mod <= 0:
            print("No puedes ingresar valores negativos, vuelve a intentarlo")
            multiplicacionModular()
        if a < mod:
            a = a % mod
        else:
            if b < mod:
                b = b % mod
        multiplicacion = a * b 
        multiplicacion = multiplicacion % mod
        return multiplicacion
    except ValueError:
        print("Debes ingresar valores numericos, vuelve a intentarlo")
        multiplicacionModular()

def divisionModular():
    try:
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo numero: "))
        mod = int(input("Ingrese el modulo (Zn): "))
        while a <= 0 or b <= 0 or mod <= 0:
            print("No puedes ingresar valores negativos, vuelve a intentarlo")
            divisionModular()
        if a < mod:
            a = a % mod
        else:
            if b < mod:
                b = b % mod
        inverso = modInverse(b,mod)
        inverso = str(inverso)
        if inverso.isdigit() == False:
            return f"Su segundo valor no tiene inverso, vuelva a intentarlo"
        else:
            inverso = int(inverso)
            division = (a * inverso) % mod
            return division
    except ValueError:
        print("Debes ingresar valores numericos, vuelve a intentarlo")
        divisionModular()

def potenciaModular():
    try:
        a = int(input("Ingrese el numero base: "))
        b = int(input("Ingrese la potencia de su numero: "))
        mod = int(input("Ingrese el modulo (Zn): "))
        while a <= 0 or b <= 0 or mod <= 0:
            print("No puedes ingresar valores negativos, vuelve a intentarlo")
            potenciaModular()
        potencia = (a ** b) % mod
        return potencia
    except ValueError:
        print("Debes ingresar valores numericos, vuelve a intentarlo")
        potenciaModular()

def raizCuadradaModular():
    try:
        valor = int(input("Ingrese el numero de la raiz: "))
        mod = int(input("Ingrese el modulo (Zn): "))
        while valor <= 0 or mod <= 0:
            print("No puedes ingresar valores negativos, vuelve a intentarlo")
            raizCuadradaModular()
        valor = valor % mod
        raices = []
        for x in range (0, mod):
            a = x * x
            if (a % mod == valor):
                raices.append(x)

        if len(raices) > 0:
            lst_raices = str(raices)[1:-1]
            print( "Las raices cuadradas son:", lst_raices)

        if len(raices) == 0:
                print( "La raiz cuadrada modular no existe, vuelve a intentarlo")
        return
    except ValueError:
        print("Debes ingresar valores numericos, vuelve a intentarlo")
        raizCuadradaModular()

def listaInversos():
    try:
        M = int(input("Ingrese el mod (Zn): "))
        if M <= 0:
            print("No puedes ingresar valores negativos, vuelve a intentarlo")
            listaInversos()

        inversos = {}
        for A in range(0,M):
            for X in range(1, M):
                operacion = (A % M) * (X % M)
                if operacion % M == 1:
                    inversos[A] = X

        if len(inversos) > 0:
            for x, y in inversos.items():
                print(f"El inverso de {x} en mod {M} es {y}")
        if len(inversos) == 0:
            print("Su numero no tiene inversos, vuelva a intentarlo")
    except ValueError:
        print("Debes ingresar valores numericos, vuelve a intentarlo")
        listaInversos()

def cuadradosPerfectos():
    try:
        mod = int(input("Ingrese el modulo (Zn): "))
        lst_cuadrados = []
        for x in range(0, mod):
            a = (x * x) % mod
            lst_cuadrados.append(a)
        lst_cuadrados = set(lst_cuadrados)
        lst_cuadrados = str(lst_cuadrados)[1:-1]
        print(f"Los cuadrados perfectos de {mod} son {lst_cuadrados}")
    except ValueError:
        print("Debes ingresar valores numericos, vuelve a intentarlo")
        cuadradosPerfectos()

#MENU DE LA CALCULADORA:
print("""
   _____      _            _           _                    __  __           _       _            
  / ____|    | |          | |         | |                  |  \/  |         | |     | |           
 | |     __ _| | ___ _   _| | __ _  __| | ___  _ __ __ _   | \  / | ___   __| |_   _| | __ _ _ __ 
 | |    / _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` |  | |\/| |/ _ \ / _` | | | | |/ _` | '__|
 | |___| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| |  | |  | | (_) | (_| | |_| | | (_| | |   
  \_____\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_|  |_|  |_|\___/ \__,_|\__,_|_|\__,_|_|                                                                                                                                                                                                      
""")
print("Bienvenido a la calculadora modular")
def menuCalculadora():
    try:
        print("1. Suma modular")
        print("2. Multiplicacion Modular")
        print("3. Division Modular")
        print("4. Potencia Modular")
        print("5. Raiz cuadrada modular")
        print("6. Lista de inversos modulares para Zn")
        print("7. Cuadrados perfectos modulares (lista y cantidad de raices)")
        print("8. Hallar el inverso de un numero en Zn")
        opcion = int(input("Ingresa la operacion que deseas realizar: "))
        print("=="*22)
        if opcion == 1:
            print("El resultado de su suma es:",sumaModular())
        elif opcion == 2:
            print("El resultado de su multiplicacion es:",multiplicacionModular())
        elif opcion == 3:
            print("El resultado de su division es:",divisionModular())
        elif opcion == 4:
            print("El resultado de su potencia modular es:",potenciaModular())
        elif opcion == 5:
            raizCuadradaModular()
        elif opcion == 6:
            listaInversos()
        elif opcion == 7:
            cuadradosPerfectos()
        elif opcion == 8:
            resultado = int(input("Ingrese un numero: "))
            mod = int(input("Ingrese el mod (Zn): "))
            print("El inverso del numero es:",modInverse(resultado,mod))
        else:
            print("Ingrese un valor valido")
            menuCalculadora()

        while True:
            newTry = input("Desea volver a intentarlo? (s/n): ")
            if newTry == "n" or newTry == "N":
                exit()
            elif newTry == "s" or newTry == "S":
                menuCalculadora()
            else:
                print("Ingrese un valor valido")
                newTry = input("Desea volver a intentarlo? (s/n): ")
    except ValueError:
        print("Debes ingresar un valor numerico, vuelve a intentarlo")
        menuCalculadora()
menuCalculadora()