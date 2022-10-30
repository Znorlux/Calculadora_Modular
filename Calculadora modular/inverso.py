def modInverse(A, M):
    try:
        for X in range(1, M):
            if (((A % M) * (X % M)) % M == 1):
                return X
        return f"No tiene inverso modular"
    except:
        print("No tiene inverso")

if __name__ == "__main__":
    try:
        resultado = int(input("Ingrese un numero: "))
        mod = int(input("Ingrese el mod (Zn): "))
        print("El inverso del nùmero es:",modInverse(resultado, mod))
    except ValueError:
        print("Debes ingresar un valor numerico")
    except NameError:
        print("Debes ingresar un valor numerico")
        