print("Ingrese el total")
total=int(input())
print("Ingrese el porcentaje de la propina deseado (10%,15%,20%)")
Propina=int(input())
print("Total de la cuenta: $",total )
totalpropina=(total*(Propina/100))
print("Total de propina: $",totalpropina)
totalpagar = total+totalpropina
print("Total a pagar de la cuenta con propina(", int(Propina),"%): $",totalpagar)