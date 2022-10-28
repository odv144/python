from definiciones import *
class tratar_binario():
    #constructor de la clase
    __archivo=""    #limito la variable al ambito de la clase
    __fb=""
    __data=""
    __contenido=""
    def __init__(self): 
        self.__archivo= ruta+"asus_k53sv.bin"
    
    def apertura_binario(self):
        self.__fb= open(self.__archivo,"rb")

    def lectura_binario(self,flag=None):
        self.__data = self.__fb.read()
        self.__contenido=bytearray(self.__data)
        if flag:
            return self.__contenido

    def buscar_cad_hex(self,cadena):
        pos= self.__contenido.find(cadena)
        if pos!=-1:
            return pos
            #print("Se encontro")
        else:
            print("No se encontro")
    
    def mostrar_binario(self):
        print(f"Datos leidos del binario {self.__data}")

f = tratar_binario()
f.apertura_binario()
rta=f.lectura_binario(True)
cadena=b'\x5a\xa5\xf0\x0f'
me=(f.buscar_cad_hex(cadena))
if me!=-1:
    print(f"se encontro en la posicion {me}")
else:
    print("No se encontro")
# f.mostrar_binario()

# #Crear una clase persona con 4 atributos y 2 propiedades y un constructor
# class Persona():
#     def __init__(self): #constructor
#         self.__nombre="Omar"
#         self.__apellido="Virili"
#         self.__edad=38
#         self.__estado="soltero"         #con el __ en el nombre de var logro encapsular para que solo
#                                         #este accesible solo dentro de la clase

#     def mostrar(self):         #self es como this pero python obliga a ponerlo
#         print(f"""
#             El nombres: {self.__nombre}     
#             El apellido: {self.__apellido}
#             La edad: {self.__edad}
#             Estado: {self.__estado}
#         """)
#         if not(self.__mayor()):
#             print("Preparece para el asilo de anciano:")

#     def modificar(self,nom,ape,edad,estado):
#         self.__nombre=nom
#         self.__apellido=ape
#         self.__edad=edad
#         self.__estado=estado
#         print("Valores de la persona cambiados")

#     def __mayor(self):              #con el doble __ tambien podemos encapsular metodos para ser accesible solo de la clase
#         if(self.__edad<18):
#             return True
#         else:
#             return False

# print("Creacion de la primera persona desde clase")

# people = Persona()
# people.mostrar()
# people.modificar("Martina","Yaccuzzi",6,"soltera")
# people.mostrar()


