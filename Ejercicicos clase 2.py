'''
Clase:        2
Tema:         Bloque condicional
Ejercicio:    Ejercicios de contraseña segura y calculo de impuesto
Descripción:  Verificar si una contraseña es segura y calcular el impuesto a pagar por un producto.

Autor:        Joshua Garcilazo
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''

#Ejercicio 1: Verificar si una contraseña es segura 
contraseña=input("Ingrese su contraseña: ")
if len(contraseña)<8:
    print("Contraseña no segura")
else: 
    for i in contraseña:
        if i.isdigit():
            Numero=True
            break
    if not Numero:
        print("Contraseña no segura")
    else:
        Mayuscula=False
        for i in contraseña:
            if i.isupper():
                Mayuscula=True
                break
        if not Mayuscula:
            print("Contraseña no segura")
        else:
                print("Contraseña segura")

#Ejercicio 2: Calcular el impuesto a pagar por un producto
unidades=int(input("Ingrese la cantidad de unidades: "))
if unidades <=100:
    print("Sin impuestos, total a pagar: $0")
elif 101<=unidades<=200:
    total1=unidades*0.5
    print("Total a pagar: ",total1)
elif unidades>=200:
    total1=unidades*0.7
    print("Total a pagar: ",total1)
