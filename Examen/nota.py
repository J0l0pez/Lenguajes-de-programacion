def otorgar_beca(promedio):
    if promedio > 95:
        print("Felicidades, se te otorgará una beca")
    else:
        print("Lo sentimos, no cumples con el promedio necesario para recibir una beca")

# Ingresa el promedio del estudiante
promedio = float(input("Ingresa el promedio del estudiante (en porcentaje): "))

# Llama a la función para otorgar la beca
otorgar_beca(promedio)