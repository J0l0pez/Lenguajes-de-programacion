def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: no se puede dividir entre 0"
    else:
        return num1 / num2

operaciones = {
    "1": suma,
    "2": resta,
    "3": multiplicacion,
    "4": division
}

print("Calculadora básica")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Seleccione una operación (1/2/3/4): ")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if opcion in operaciones:
    resultado = operaciones[opcion](num1, num2)
    print("El resultado es:", resultado)
else:
    print("Opción inválida")