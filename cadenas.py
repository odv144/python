#Ejercicio 1 ingres una cadena y la imprime tantas veces como indica el nro 
# nombre = input("Ingrese el nombre: ")
# nro = int(input("Ingrese un numero entero: ")) 
# print((nombre + "\n") * nro)

# for x in range(nro):
#    print(f"{nombre}")
#---------------------------------------------
# ##Ejercicio 2 
# nombre =str(input("Ingrese nombre y apellido comleto: "))
# print(nombre.upper())   #cambia todo a mayuscula
# print(nombre.lower())   #cambia todo a minuscula
# print(nombre.title())   #cambia la primera a mayuscula 
# #///////////////////////////////////////////////////
# Ejercicio 3
# nombre =(input("Ingrese nombre y apellido comleto: "))
# cantidad= len(nombre)
# print(f"{nombre.upper()} Tiene {cantidad} de letras")
#////////////////////////////////////////////////////
# #Ejercicio 4
# #tel = input("Ingrese el numero telefonico: ")
# tel = "+549-3482558453-9"
# # telsin = tel.removeprefix("+549-")
# # telsin = telsin.removesuffix("-9")
# tels=tel[5:-2]
# print(f"{tels}")
#////////////////////////////////////////////////////
# Ejercicio 5
# cadena = input("Ingrese la cadena: ")
# print(cadena[::-1])
# #////////////////////////////////////////////////////
# Ejercicio 6
# frase = input("Ingrese la frase: ")
# vocal = input("Ingrese la letra")
# print(frase.replace(vocal,vocal.upper()))
##////////////////////////////////////////////////////
# Ejercicio 7
# email = input("Ingrese el email: ")
# pos = email.find("@")           #busco la posicion del arroba
# print(email[:pos]+"@ceu.es") #rebano el mail hasta el @ y luego lo concateno
##////////////////////////////////////////////////////
# Ejercicio 8
# precio = (input("Ingrese el precio del producto: "))
# print(f"{precio[0:precio.find(',')]} Euros con {precio[precio.find(',')+1:]} centimos")
##////////////////////////////////////////////////////
# # Ejercicio 9
# #fecha = input("Ingrese su fecha de nacimiento: ")
# fecha = "28/02/1984"
# dia = fecha[:fecha.find('/')]
# mes = fecha[fecha.find('/')+1:]
# anio = mes[fecha.find('/')+1:]
# mes = mes[:mes.find('/')]
# print(f"Nacimio el día {dia} del mes {mes} del año {anio}")
# ##////////////////////////////////////////////////////
# Ejercicio 10
# cesta = "manteca,perra,limon,tomate"
# print(cesta.replace(',','\n'))

#////////////////////////////////////////////////////
# Ejercicio 11
# detalle = input("Ingrese producto: ")
# p_u = float(input("Ingrese precio unitario "))
# cant = int (input("Ingrese cantidad "))
detalle = "Javon en Polvo"
p_u= 250,90
cant = 3.5015
print('detalle:  cantidad {cant:3.3f}'.format(cant=cant))
#////////////////////////////////////////////////////
#////////////////////////////////////////////////////