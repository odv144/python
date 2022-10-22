
from definiciones import *
fin=True
while fin:
    print("""
        ****************************************
        Menu Principal para Edicion de Bios
        ****************************************
        1-Deshabilitar Ram Onboard
        2-Desbloqueo Dell 8FC8-8FD8
        9-Salir        
        """)
    op = int(input("Ingrese opcion elegida: "))
    
    if op==1:
        archivo = open("d:/python/asus_k53sv.bin","rb")
        nuevo = open("d:/python/mibios.bin","wb")
        byte = 0
        reading = bytearray(archivo.read())
        end_file=len(reading)

        flag= True
        while flag:
            pos=reading.find(RegionMe)
            if pos!=-1:
                print(f"cadena buscada{buscar}\n Se encontro en la posicion {pos} \n y se modificaron 1000 valores por FF")
                for x in range(0,8):
                    reading[pos+x]=reemplazo[x]
            else:
                # print(f"cadena buscada{buscar}\n NO SE ENCONTRO\n y se modificaron 1000 valores por FF")
                flag=False  

        nuevo.write(reading)
        nuevo.close()
        archivo.close()
    elif op==2:
        pass
    elif op==9:
        fin = False


# for x in range(end_file):
#        if reading.find(b'\x5a\xa5\xf0\x0f\x03\x01',posicion,end_file):
# #     # posicion = reading[1000:100000].find(b'\x00\xfd\xaa') # busco en las posiciones esa cadena
#         print(f"Encontro con 5AA5 en pos {posicion}")
#     posicion +=x
        
 
# print(hex(primeros_1000))
# reemplazo=b'\xe5\xf4\xb3' #cadena con la que reemplazo
# nuevo.write(reading[:primeros_1000])
# nuevo.write(reemplazo)
# nuevo.write(reading[primeros_1000+3:])

# si llegue aqui la cade 00FCAA o 00FDAA aparecio y entonces debemos cambiar AA por 00

"""
# si es intel  el comienzo siempre  4kb descriptor
# 4096
16 primeros con ff y luego 5AA5F00F INDICACION DE INTEL comienzo descripto
primeros 4096
luego comienzo comienzo me region 2097152 --  oem seccion 
ME REGION -> 2020000f40 -> 
TERMINA -> BIOS REGION -> DEPENDE DEL FABRICANDO
"""