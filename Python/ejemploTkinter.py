"""from tkinter import*
def hola():
    print("Hola"+" "+nombre.get()+" "+apellido.get()+" "+"como estas")


root=Tk()
root.title("Ventana")
#root.resizable(0,0)"""

"""frame=Frame(root,width=400,height=400)
frame.pack()
frame.config(bg="red")
#root.mainloop()"""

"""nombre=StringVar()
apellido=StringVar()
Label(root,text="Ingresa tu nombre: ").pack()
Entry(root,justify=CENTER,textvariable=nombre).pack()
Label(root,text="Ingresa tu apellido: ").pack()
Entry(root,justify=CENTER,textvariable=apellido).pack()


Button(root,text="Click aqui mano",command=hola).pack()

root.mainloop()"""


"""from tkinter import *

def hola():

    mensaje.set("HOLA "+ nombre.get())

root=Tk()

root.title("Ventana")

nombre=StringVar()
mensaje=StringVar()

Label(root,text="ingresa tu nombre:").pack()
Entry(root,justify=CENTER, textvariable=nombre).pack()
Label(root,text="MENSAJE:").pack()
Label(root,justify=CENTER, textvariable=mensaje).pack()

Button(root,text="INGRESAR NOMBRE",command=hola).pack()

root.mainloop()"""