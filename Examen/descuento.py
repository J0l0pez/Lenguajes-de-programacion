def calcular_descuento(precio):
    if precio > 500:
        descuento = precio * 0.10
        precio_con_descuento = precio - descuento
        return precio_con_descuento
    else:
        return precio

def main():
    precio = float(input("Ingrese el precio del producto en córdobas: "))
    precio_final = calcular_descuento(precio)
    print(f"El precio final con el descuento aplicado es: {precio_final:.2f} córdobas")

if __name__ == "__main__":
    main()