from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk


#----------------frame---------------------
def marco():
    
    """agrego el frame a la raiz para posicionar el frame side y anchor anchor tiene valores cardinales n-s-w-e-ne-nw-se-sw"""
    #frame.pack(side="left", anchor="n")                
    """fill redimenciona en x si esta solo fill=x, para redimencionar y fill="y", expand=True """
    #frame.pack(fill="y", expand="True") 
    """si quiero redimencionar tanto x y uso fill="both" y expand=True """
    frame.pack(fill="both", expand="False")
    frame.config(bg="green")                                 
    frame.config(width="350", height="200") #establecer color de fonde del frame
    """para cambiar el tamaño del borde"""
    frame.config(bd=5)
    """para cambiar el estilo de linea """
    frame.config(relief="sunken")
    """para cambiar la distancia desde el margen"""
    frame.config(padx=5,pady=5)
    """para cambiar el cursor en una zona en este caso cuando este sobre el frame"""
    #frame.config(cursor="pirate")
    """crea una etiqueta para mostrar texto o imagen"""
#---------------inicio funcion--etiqueta----------------
def etiqueta():
    lblPantalla=Label(frame,text="Display de calculadora")
    lblPantalla.grid(row=0,column=0)
    lblPantalla.config(bg="green")
    lblPantalla.config(padx=5)
    lblDato=Label(frame,text="Dato a mostrar")
    lblDato.grid(row=0,column=1)
    return lblDato
    #no pude poner imagen
    # miImagen=PhotoImage(file="placa.jpg")
    # Label(frame,image=miImagen).grid(row=2,column=2)
#////////////////fin funcion--etiqueta//////////////////

#---------------inicio funcion--caja texto----------------
def cajaTexto():
    nombre = StringVar()
    txtArchivo = Entry(frame,textvariable=nombre)
    txtArchivo.insert(0,"c:/nombre_archivo.bin")         #forma para insertar texto en la caja
    txtArchivo.grid(row=1,column=0)
    return txtArchivo #leo lo que se escribio en la caja
    
#////////////////fin funcion--caja texto//////////////////
#---------------inicio funcion--boton----------------
def boton(dato,lblEti):
    #para que el boton pueda cambiar el valor de text del label debo acceder a su propiedad config
   btnPrueba = Button(frame,text="Mostrar contenido",command=lambda:lblEti.config(text=dato.get()))
#    btnPrueba.config(padx=5,pady=5)
   btnPrueba.grid(row=1,column=1)
#////////////////fin funcion--caja boton//////////////////
#---------------inicio funcion--combobox----------------
def listado():
    lista = StringVar()
    cmbLista = ttk.ComboBox(frame,textvariable=lista)
    cmbLista['values']=("Argentina","Peru","Chile")
    cmbLista.grid(row=2,column=0)
   
    
#////////////////fin funcion--combobox//////////////////

#---------------inicio programa-ventana----------------------
raiz = Tk()                         #creo la ventana
raiz.title("Edicion de Bios")       #Pongo titulo a la ventana
raiz.iconbitmap("autorun.ico")      #pongo icono a la ventana
#raiz.geometry("800x600")            #establece el tamaño de la ventana si uso frame debe quitar
raiz.config(bg="grey")              #color de fondo de la ventana
frame = Frame()

marco() #llamo a la funcion para crear el frame
lblEti = etiqueta() # funcion para crear label

dato = cajaTexto()   #llamada funcion para agregar caja de texto
boton(dato,lblEti)
# listado()
raiz.mainloop()