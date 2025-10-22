fruta = "manzana"

match fruta:
    case "manzana":
        print("es una manzana")
    case "pera":
        print("es una pera")
    case _:
        print("fruta desconocida")


color = input("ingrese un color: ")

match color:
    case "amarillo":
        print("yellow")
    case "azul":
        print("blue")
    case "rojo":
        print("red")
    case _:
        print("unidentified color")

numero1 = int(input("ingrese un numero: "))
numero2 = int(input("ingrese otro numero: "))

operaciones = input('ingrese operacion: ')

match operaciones:
    case "suma":
        suma = numero1+numero2
        print(f"resultado es: {suma}")
    case "resta":
        resta = numero1-numero2
        print(f"la resta es: {resta}")
    case "multiplicar":
        multiplicar = numero1*numero2
        print(f"multiplicacion es: {multiplicar}")
    case "division":
        division = numero1/numero2
        print(f"la divicion es: {division}")
    case _:
        print("no se identifica operacion")            
