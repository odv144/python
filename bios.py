
archivo = open("e:/la-j371pp.bin","rb")
nuevo = open("e:/mibios.bin","wb")
byte = 0
reading = (archivo.read())
end_file=len(reading)
x = 0

posicion = 0
for x in range(end_file):
    # posicion = reading[posicion:].find(b'\x5a\xa5\xf0\x0f\x03\x01') # busco en las posiciones esa cadena
# # print("econtro con fc")
 
    
    if reading.find(b'\x5a\xa5\xf0\x0f\x03\x01',posicion,end_file):
#     # posicion = reading[1000:100000].find(b'\x00\xfd\xaa') # busco en las posiciones esa cadena
        print(f"Encontro con 5AA5 en pos {posicion}")
    posicion +=x
        
 
# print(hex(primeros_1000))
# reemplazo=b'\xe5\xf4\xb3' #cadena con la que reemplazo
# nuevo.write(reading[:primeros_1000])
# nuevo.write(reemplazo)
# nuevo.write(reading[primeros_1000+3:])

# si llegue aqui la cade 00FCAA o 00FDAA aparecio y entonces debemos cambiar AA por 00