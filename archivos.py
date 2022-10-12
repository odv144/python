# archivo = open("e:/prueba2.txt","w")
# x=0
# tupla = ["Matematica","Lengua","Programacion"]
# while x<10:
#     archivo.write(f"Linea {x} de 100\n")
#     x+=1
# archivo.write(str(tupla))
# dicionario = {"clave":"valor","nombre":"Omar Dario","apellido":"Virili","edad":38}
# dicionario["nombre"]="Jorge"
# archivo.write(str(dicionario))

# archivo.close

archivo = open("e:/la-j371pp.bin","rb")
byte = 0
while byte<64:
    # print(archivo.read(8),end="-")
    # if(byte==4):
    #     archivo.write("\xFF")
    if byte == 16:
        byte= 7
    archivo.seek(byte,0)    
    print(archivo.read(8),end="-")
    byte+=8
