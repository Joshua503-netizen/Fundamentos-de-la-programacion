print("Ingrese su nombre")
nombre=input(str())
print("Ingrese su apellido")
apellido=input(str())

nombresinespacios=nombre.replace(" ", "")
apellidosinespacios=apellido.replace(" ", "")
nombresinespacios2=nombresinespacios.lower()
apellidosinespacios2=apellidosinespacios.lower()
resultado=nombresinespacios2 + "." + apellidosinespacios2 + "@keyinstitute.edu.sv"
print("El correo que se debe asignar al usuario ingresado es:",resultado)