from io import BytesIO
# archivo = open("e:/prueba2.txt","wb")
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


archivo = open("e:/main_u5_original_sin_video.bin","rb")
nuevo = open("e:/mibios.bin","wb")
byte = 0
archivo.seek(byte,0)    
reading = archivo.read()
primeros_1000 = reading[:1000].find(b'\x91\xf0\x0A\xFF\xF7'+ b'\xfc' * 0x03) # busco en las posiciones esa cadena
print(hex(primeros_1000))
reemplazo=b'\xe5\xf4\xb3' #cadena con la que reemplazo
nuevo.write(reading[:primeros_1000])
nuevo.write(reemplazo)
nuevo.write(reading[primeros_1000+3:])
# if(b'\x5A\xA5\xf0' in primeros_256):
#     nuevo.write(reading[:512])
# else:
#     nuevo.write(b'\xbb')
# nuevo.write(reading) # escribo en el archivo nuevo todo el contenido leido en la variable
# file_end = len(reading) # Store the input file buffer Size/EOF
# reading_16 = reading[:0x10] # Store the first 16 input file buffer bytes
# leo = reading[:0x100]
# print(file_end)
# nuevo.write(leo)#con esto copio todo el archivo que lei
# nuevo.write(b'\xaa\x55')
# leo = reading[0x101:0x120]
# nuevo.write(leo)

archivo.close()
nuevo.close()

# if reading[:0x0a] == b'\x10\x00\x00\xf7\x10\x05\x00\xb6\xff\xff' :    
#     archivo.seek(0)
#     archivo.write(b"\x10")#reemplazo el valor de x10 por xfb en la posicion 0
#     print(f"es igual")
# else:
#     archivo.seek(0)#muevo a la posicion que necesito para escribir
#     archivo.write(b"\x10")
#     print(f"es distinto")
# archivo.close()


# while byte<64:
#     # print(archivo.read(8),end="-")
#     # if(byte==4):
#     #     archivo.write("\xFF")
#     if byte == 16:
#         byte= 7
#     archivo.seek(byte,0)    
#     print(archivo.read(8),end="-")
#     byte+=8
