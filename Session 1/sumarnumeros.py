def sumar_digitos():
  numero = input("Ingrese un numero: ")
  suma = sum(int(digit) for digit in numero if digit.isdigit())

  return f"La suma de los digitos es de: {numero} es: {suma}"

print(sumar_digitos())