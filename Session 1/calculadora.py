# calculatora 
def calculatora ():
    
    num1 = int(input("Ingrese el primer numero:"))
    num2 = int(input("Ingrese el segundo numero:"))
    
    operacion = input(str("Ingrese la operacion:\n 1.Suma\n 2.Resta\n 3.Multiplicacion\n 4.Division\n Ingrese el numero de la operacion: ----> "))

    if operacion == "1":
        return f"El resultado de la suma es: {num1 + num2}"
    elif operacion == "2":
        return f"El resultado de la rsta es: {num1 + num2}"
    elif operacion == "3":
        return f"El resultado de la multiplicación es: {num1 + num2}"
    elif operacion == "4":
        return f"El resultado de la división es: {num1 + num2}"
    else:
        return "Operacion "

# call the function use print to show the result
print(calculatora())    