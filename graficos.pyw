from tkinter import *
#----------------ventana----------------------
raiz = Tk()                         #creo la ventana
raiz.title("Edicion de Bios")       #Pongo titulo a la ventana
raiz.iconbitmap("autorun.ico")      #pongo icono a la ventana
#raiz.geometry("800x600")            #establece el tamaño de la ventana si uso frame debe quitar
raiz.config(bg="grey")              #color de fondo de la ventana
#----------------frame---------------------
frame = Frame()
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
lblPantalla=Label(frame,text="Display de calculadora")
lblPantalla.grid(row=0,column=0)
lblPantalla.config(bg="green")
lblPantalla.config(padx=5)
lblDato=Label(frame,text="Dato a mostrar")
lblDato.grid(row=0,column=1)
#no pude poner imagen
# miImagen=PhotoImage(file="placa.jpg")
# Label(frame,image=miImagen).grid(row=2,column=2)



raiz.mainloop()