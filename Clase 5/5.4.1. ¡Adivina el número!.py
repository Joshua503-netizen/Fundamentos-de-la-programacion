'''
Clase:        6
Tema:         Uso de bucles indefinidos
Ejercicio:    Adiivinar el número
Descripción:  Adiivinar el número que sea ingresado por el usuario, si es correcto se imprime un mensaje de felicitación, si no, se pide que vuelva a intentarlo.

Autor:        Joshua Garcilazo
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''

import random
a=range(1,101)
numero=random.choice(a)
print("Adivina le numero entre 1 y 100")
while True:
    numeroelegido=int(input("Ingrese un numero entre 1 y 100: "))
    if numeroelegido > numero:
        print("El numero es menor que:", numeroelegido)
    if numeroelegido < numero:
        print("El numero es mayor que: ", numeroelegido)
    if numeroelegido==numero:
        print("Felicidades, adivinaste el numero:", numeroelegido)
        break
          