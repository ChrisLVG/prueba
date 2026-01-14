# Adivinar el numero
import random
numero = random.randint(1,10)
print("adivina el numero entre 1 y 10")
adivina = int(input("ingresa tu numero: "))
while adivina != numero:
    if adivina < numero:
        print("muy bajo")
        print("intenta de nuevo, el numero fue:", numero)
    elif adivina > numero:
        print("muy alto")
        print("intenta de nuevo, el numero fue:", numero)
    adivina = int(input("ingresa tu numero: "))
print("felicidades, adivinaste el numero:", numero)
