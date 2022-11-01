# manejo de cajero
datos={"clave":"1234","ayn":"Virili Omar Dario","saldo":25000,"saldoDolar":500,"plazofijo":{"f_ini":"22-10-2022","f_fin":"22-11-2022","monto":30000}}

def menu():
    print(
        """
        MENU DE OPCIONES DEL CAJERO
        # 01-CONSULTA SALDO
        # 02-DEPOITAR DINERO
        # 03-EXTRAER DINERO
        # 04-TRANSFERIR DINERO
        # 05-COMPRAR DOLARES
        # 06-VENDER DOLARES
        # 07-CREAR PLAZO FIJO
        # 08-ULTIMOS MOVIMIENTOS
        # 09-PAGAR SERVICIOS
        # 10-SALIR
        """
    )
    fin=True
    op=int(input("Ingrese una opcion: "))
    if op==1:
        print("------------------SALDO--------------------")
        print(f"Su saldo en Pesos es: {datos['saldo']}")
        print(f"Su saldo en Dolares: {datos['saldoDolar']}")
        print(f"Su saldo en Plazo Fijo: {datos['plazofijo']['monto']}")
        print("////////////////////////////////////////")
    if op==2:
        print("--------------DEPOSITAR DINERO------------")
        caja = int(input(
                """Seleccione la cuenta a la cual depositara
                1-Pesos
                2-Dolares
                3-Plazo fijo"""))
        if caja ==1:
            print("Caja en Pesos")
            
        elif caja ==2:
            print("Caja en Dolares")
            
        else:
            print("Plazo fijo")
        print(f"Su saldo en Pesos es: {datos['saldo']}")
        print(f"Su saldo en Dolares: {datos['saldoDolar']}")
        print(f"Su saldo en Plazo Fijo: {datos['plazofijo']['monto']}")
        print("////////////////////////////////////////")
    # if op==3:
    #     pass
    # if op==4:
    #     pass
    # if op==5:
    #     pass
    # if op==6:
    #     pass
    # if op==7:
    #     pass
    # if op==8:
    #     pass
    # if op==9:
    #     pass
    if op==10:
        fin=False
    return fin

def cajero():
    flag= True
    print("*********************")
    if(input("Ingrese Clave: "))== datos["clave"]:
        while flag:
            flag=menu()

cajero()
