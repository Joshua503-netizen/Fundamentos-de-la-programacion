'''
Clase:        1
Tema:         Variables
Ejercicio:    Ejercicios de contraseña segura y calculo de impuesto
Descripción:  Calcular la propina de una cuenta y crear un correro electronico

Autor:        Joshua Garcilazo
Fecha:        2025-05-22
Estado:       [ Terminado ]
'''

#Ejercicio 1: Calcular la propina de una cuenta
total=int(input(("Ingrese el total: ")))
Propina=int(input(("Ingrese el porcentaje de la propina deseado (10%,15%,20%)")))
print("Total de la cuenta: $",total )
totalpropina=(total*(Propina/100))
print("Total de propina: $",totalpropina)
totalpagar = total+totalpropina
print("Total a pagar de la cuenta con propina(", int(Propina),"%): $",totalpagar)

#Ejercicio 2: Crear un correro electroncio
nombre=str(input("Ingrese su nombre: "))
apellido=str(input("Ingrese su apellido: "))
nombresinespacios=nombre.replace(" ", "")
apellidosinespacios=apellido.replace(" ", "")
nombresinespacios2=nombresinespacios.lower()
apellidosinespacios2=apellidosinespacios.lower()
resultado=nombresinespacios2 + "." + apellidosinespacios2 + "@keyinstitute.edu.sv"
print("El correo que se debe asignar al usuario ingresado es:",resultado)
