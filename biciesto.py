
anio = int(input("Ingrese año "))
if anio >0:
    if (anio % 4 ==0):
            print(f"El año {anio} es biciesto")
    else:
            print(f"El año {anio} no es biciesto")
else:
        print("El año introduccido es incorrecto")