
import random

def guessNumber():
    print("Adivina el numero")
    # generar numero aleatorio con la libreria random y el metodo randint
    numero = random.randint(1, 20)
    
    # ciclo while para adivinar el numero
    while True:
        adivina = int(input("Adivina :"))
        # pista para el usuario de muy bajo
        if adivina < numero:
            print("Muy bajo")
        # pista para el usuario de muy alto
        elif adivina > numero:
            print("Muy alto")
        else:
            break
    # mensaje de felicitaciones si adivina el numero
    if adivina == numero:
        print("Adivinaste")

    print("Fin del juego")

guessNumber()