#Pedir al usuario que ingrese el capital y el interes anual que genera una comicion bancaria, tambien pedir la cantidad de años que dejara el deposito
capital=float(input("Ingrese el capital "))
interes = float(input("Ingrese interes "))
tiempo = int(input("Ingrese cantidad de años "))
acumulado=capital
for tiempo in range(1,tiempo+1):
    print(f"Total acumulado el año {tiempo} es: ${(acumulado + acumulado * interes/100):5.2f}")
    acumulado = acumulado + (acumulado * interes/100)
print(f"El total acumulado en todo el tiempo sera: ${acumulado:7.2f}")