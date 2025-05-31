'''
Clase:        6
Tema:         Bucles y control de flujo.
Ejercicio:    Sumador de valores posicionales
Descripción:  Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito.
Autor:        Joshua Garcilazo
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''

numero=int(input("Ingrese un numero: "))
while True:
    if len(str(numero)) > 1:
        suma=0 
        for i in str(numero):
            suma += int(i)
        numero = suma
    if len(str(numero))==1:
        print("El resultado es:", numero)
        break
#1