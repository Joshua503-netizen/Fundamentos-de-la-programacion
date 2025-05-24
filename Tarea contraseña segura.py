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