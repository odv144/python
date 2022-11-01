# anio = int(input("Ingrese año "))
# if anio >0:
#     if (anio % 4 ==0):
#             print(f"El año {anio} es biciesto")
#     else:
#             print(f"El año {anio} no es biciesto")
# else:
#         print("El año introduccido es incorrecto")

from struct import *
import ctypes
import struct
class Registros():
    campos = [
            ('name', ctypes.c_char*20),
            ('edad', ctypes.c_int),
            ('sueldo', ctypes.c_int32),
            ]

# record = b'raymond   \x32\x12\x08\x01\x08'
archivo = open('empleados2.bin',"rb")
data = bytearray(archivo.read())
s = Registros
slen = 56

for x in range(0,(len(data)),28):
    datos = data[x:x+26]
    s.campos[0],s.campos[1],s.campos[2] = unpack('<20sHf',datos)
    print(f"Nombre: {s.campos[0]} Edad: {s.campos[1]} Sueldo: {s.campos[2]}")
# from collections import namedtuple
# Student = namedtuple('studen', 'name serialnum school gradelevel')
# Student._make(unpack('<10sHHb', record))




