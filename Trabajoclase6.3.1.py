'''
Clase:        6
Tema:         Aprendiendo con listas
Ejercicio:    Eliminando valores duplicados de una lista
Descripción:  Eliminar los numeros duplicados de una lista y mostrar la lista resultante.

Autor:        Joshua
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''


lista = list(map(int, input().split(' ')))
listasin = list(set(lista))
print("Lista sin duplicaditos:", listasin)
lista2 = list(map(int, input().split(' ')))
l = []
for i in lista2:
    if i not in l:
        l.append(i)