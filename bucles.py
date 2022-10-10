#Pedir al usuario que ingrese el capital y el interes anual que genera una comicion bancaria, tambien pedir la cantidad de años que dejara el deposito
# capital=float(input("Ingrese el capital "))
# interes = float(input("Ingrese interes "))
# tiempo = int(input("Ingrese cantidad de años "))
# acumulado=capital
# for tiempo in range(1,tiempo+1):
#     print(f"Total acumulado el año {tiempo} es: ${(acumulado + acumulado * interes/100):5.2f}")
#     acumulado = acumulado + (acumulado * interes/100)
# print(f"El total acumulado en todo el tiempo sera: ${acumulado:7.2f}")

# #////////////////////////////////////////////////////////////
# # Pida al usuario un numero y genere un triangulo del asteriscos
# #Ejercicio 6
# nro = int(input("Ingrese la altura del triangulo: "))
# for x in range(1,nro+1):
#     print(("*") * x)
# #////////////////////////////////////////////////////////////
# # Pida al usuario un numero y genere un triangulo del asteriscos
# #Ejercicio 7
# for x in range(1,10):
#     print(f"La tabla del {x} es la siguiente")
#     for y in range(1,11):
#         print(f"{y} x {x} = {y*x}")
#     print("----------------------")

# #////////////////////////////////////////////////////////////
# # Pida al usuario un numero y genere un triangulo rectangulo como el siguiente
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# #Ejercicio 8 
# nro = int(input("Ingrese un nro entero: "))
# tri=""
# for x in range(1,nro+1,2):
#     tri = str(x)+" "+ tri
#     print (f"{tri}")
# #////////////////////////////////////////////////////////////
#Ejercicio 9
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
# password = "seguridad"
# password2 =""
# while password != password2:
#     password2 = input("Ingrese el password ")
#////////////////////////////////////////////////////////////
#Ejercicio 10
#escribe una frase ingresada al reves
# frase=input("Ingrese una frase o palabra: ")
# for letra in range(len(frase)-1,-1,-1):
#     print(frase[letra], end=" ")
#////////////////////////////////////////////////////////////
#Ejercicio 11
# frase = input("Ingrese una frase: ")
# letra = input("Ingrese una letra a buscar:")
# con =0
# for x in range(len(frase)):
#     if letra == frase[x]:
#         con=con+1
# print(f"La cantidad de letras '{letra}' que aparece en la frase es: {con}")
# #////////////////////////////////////////////////////////////
#Ejercicio 12 solucion 1
# palabra = ""
# while(palabra != "salir"):
#     palabra = input("Ingrese una palabra: ")
#     print(palabra)
#Solucion 2
while True:
    palabra = input("Ingrese una palabra: ")
    if (palabra == "salir"):
        break
    print(palabra)
#////////////////////////////////////////////////////////////