# Description: Convertidor de divisa
def obtener_divisa(cambio):
  # Divisa: USD, EUR, NIO
  divisa = {
    ("USD", "NIO"): 36.60,
    ("EUR", "NIO"): 20.10,
  }

  return divisa.get(cambio, None)

# convertir divisa

def convertir_divisa():
  
  # obtener los datos del usuario
  cantidad = float(int(input("Ingrese la cantidad:")))
  moneda_cambio = input("Introduce la moneda de origen (USD, EUR, NIO): ").upper()
  moneda_destino = input("Introduce la moneda que deseas convertir (USD, EUR, NIO): ").upper()

  # obtener divisa
  tasa = obtener_divisa((moneda_cambio, moneda_destino))

  # calculo de divisa
  if tasa:
    resultado = cantidad * tasa
    return f"{cantidad} {moneda_cambio} = {resultado} {moneda_destino}"
  else:
    return "Divisa invalida"
  
print(convertir_divisa())