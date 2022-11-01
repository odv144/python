# import ctypes
# import binascii
# import struct
# import sys
# import os
# import array
# from struct import calcsize

# def read_struct(li, estructura):
#     s = estructura
#     slen = ctypes.sizeof(s)
#     bytes = li.read(slen)
#     # edad = bytes[65:67]
#     unpacket = struct.unpack(ctypes.create_string_buffer(slen),bytes)
    
#     return unpacket
#     def __init__(self):
#         self.Offset = None



# archivo = open("F:/programacion web/python/archivo1.bin","rb")

# data=read_struct(archivo,tamRegDatos)
# print(data)


# values = (520, 'abCnose pore que no me aumenta'.encode('utf-8'), 2.7)
# s = struct.Struct('l 12s f')
# packed_data = s.pack(*values)
# unpa=binascii.hexlify(packed_data)
# print('Original values:', values)
# print('Format string  :', s.format)
# print('Uses           :', s.size, 'bytes')
# print('Packed Value   :', unpa)

# import struct
# import binascii
# archivo = open("F:/programacion web/python/archivo1.bin","rb")

# data=archivo.read()
# packed_data = binascii.unhexlify(binascii.hexlify(data))
# ldata = len(packed_data)
# s = struct.Struct('<50s 14s i f')
# unpacked_data = s.unpack()
# print('Unpacked Values:', unpacked_data)

import ctypes
import struct
import sys
import os
import array

int_t      =ctypes.c_int
uint8_t  = ctypes.c_ubyte
char     = ctypes.c_char
uint32_t = ctypes.c_uint
uint64_t = ctypes.c_uint64
uint16_t = ctypes.c_ushort
float_t= ctypes.c_float

class tamRegDatos(ctypes.LittleEndianStructure):
    fields = [
        ("ayn",            char*50),   # $MME
        ("tel",            char*15), #
        ("edad",           int_t), #
        ("sueldo",         float_t), #
        
    ]

def get_struct(str_, off, registro):
    s = registro
    # off=76*2
    slen = 76
    bytes = str_[off:off+slen]
  
    s.fields[0], s.fields[1], s.fields[2], s.fields[3] = struct.unpack('50s15sif', bytes)
    print(f"Nombre: {s.fields[0]},\n Telefono: {s.fields[1]},\n Edad: {s.fields[2]}, \n Sueldo: {s.fields[3]}")
    
    # fit = min(len(bytes), slen)
    # if fit < slen:
    #     raise Exception("can't read struct: %d bytes available but %d required" % (fit, slen))
    # ctypes.memmove(ctypes.addressof(s), bytes, fit)
    
    # return bytes


archivo = open("F:/programacion web/python/archivo1.bin","rb")
data=bytearray(archivo.read())


get_struct(data,76*2,tamRegDatos)
# s=struct.Struct('50s 15s i f')

