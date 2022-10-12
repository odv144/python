# #Ejercicio 1 crea una tupla con las materias de un colegio
# materia=["Matemática","Lengua","Quimica","Ingles","Programación"]
# print(materia)
# # ////////////////////////////////////
#Ejercicio 2
"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> 
es cada una de las asignaturas de la lista.
"""
# materia = ["Matemática","Lengua","Quimica","Ingles","Programación"]
# for x in materia:
#     print(f"Yo estudio {x}")

 # ////////////////////////////////////
#Ejercicio 3
""" Almacene las asignaturas de un curso en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una 
de las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario. """
# materia = ["Matemática","Lengua","Quimica","Ingles","Programación"]
# nota=[]
# for x in materia:
#     nota.append(input(f"Introduce la nota sacada en: {x} "))
# i=0
# for x in materia:
#     print (f"La nota de {x} es \t {nota[i]}")    
#     i = i+1
#////////////////////////////////////
#Ejercicio 4
""" Escribir un programa que pregunte al usuario los 10 primeros números ganadores de la lotería nacional, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. """
# lista = []
# for x in range(10):
#     lista.append(int(input(f"Ingrese el nro {x+1}: ")))
# lista.sort()
# print(f"El numero mayor de los ganarodes es {lista}")
# #////////////////////////////////////
# Ejercicio 5
# lista=[1,2,3,4,5,6,7,8,9,10]
# lista.reverse()
# for x in range(10,0,-1):
#     print(x,end=",")

#////////////////////////////////////
# Ejercicios 6
"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y 
elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas 
que el usuario tiene que repetir."""
# materia = ["Matemáticas","Física","Química", "Historia","Lengua"]
# nota = []
# for x in range(len(materia)):
#     nota.append(int(input(f"Ingrese la nota para {materia[x]} ")))

# for x in range(len(materia)):
#     if nota[x]>6:
#         materia.remove(materia[x])
    
# print("Materias que debe recursar: ")
# print(materia)
# #////////////////////////////////////
#Ejercicio 7
"""Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen 
posiciones múltiplos de 3, y muestre por pantalla la lista resultante."""
# abc=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# for x in range(len(abc),1,-1):     #esta solucion no permite remover el elemento porque recorre la lista completa
#     if(x % 3 == 0):             #y si eliminamos termina saliendo de rango el indice
#         abc.pop(x-1)
# print(abc)

# #////////////////////////////////////
# #Ejercicio 8
# """Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo."""
# palabra = input("Ingrese una palabra: ")
# palabra = list(palabra.upper())
# pal = list(palabra)
# pal.reverse()

# if palabra == pal:
#     print(f"La palabra es palindromo")
# else:
#     print("La palabra no es palindromo")
# #////////////////////////////////////
#ejercicio 9
""" Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces 
que contiene cada vocal."""
# frase = input("Ingrese una palabra o frase")
# vocal = ["a", "e","i","o","u"]
# for x in range(len(vocal)):
#     print(f"La vocal {vocal[x]} aparece {frase.count(vocal[x])} veces") 
#////////////////////////////////////
#Ejercicio 10
"""Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y
muestre por pantalla su producto escalar. """
# v1 = [1,2,3]
# v2 = [-1,0,2]
# total = 0
# for x in range(len(v1)):
#     total = total + (v1[x]*v2[x])
# print(f"El valor es {total}")
#////////////////////////////////////
#Ejercicio 11
"""
"""
#////////////////////////////////////