from tkinter import *
 
root = Tk()
root.title('Ferretería El tornillo feliz')
 
miFrame = Frame(root)
miFrame.pack()
#------- Label y entry DNI --------------------------------
obtenerDni=StringVar()
lDni = Label(miFrame, text='DNI:')
lDni.grid(row=0, column=0, sticky='e', pady=5, padx=5)
tDni = Entry(miFrame,textvariable=obtenerDni)
tDni.grid(row=0, column=1, pady=5, padx=5)
#------- Label y entry Apallido --------------------------------
obtenerApellido=StringVar()
lApellido = Label(miFrame, text='Apellido:')
lApellido.grid(row=1, column=0, sticky='e', pady=5, padx=5)
tApellido = Entry(miFrame,textvariable=obtenerApellido)
tApellido.grid(row=1, column=1, pady=5, padx=5)
#------- Label y entry Nombre --------------------------------
obtenerNombre=StringVar()
lNombre = Label(miFrame, text='Nombre:')
lNombre.grid(row=1, column=2, sticky='e', pady=5, padx=5)
tNombre = Entry(miFrame,textvariable=obtenerNombre)
tNombre.grid(row=1, column=3, pady=5, padx=5)
#------- Label y entry Dirección --------------------------------
obtenerDir=StringVar()
lDireccion = Label(miFrame, text='Dirección:')
lDireccion.grid(row=2, column=0, sticky='e', pady=5, padx=5)
tDireccion = Entry(miFrame,textvariable=obtenerDir)
tDireccion.grid(row=2, column=1, columnspan=3, sticky='we',pady=5, padx=5)
#------- Label y entry Teléfono --------------------------------
obtenerTel=StringVar()
lTel = Label(miFrame, text='Teléfono:')
lTel.grid(row=3, column=0, sticky='e', pady=5, padx=5)
tTel = Entry(miFrame,textvariable=obtenerTel)
tTel.grid(row=3, column=1,columnspan=3, sticky='we', pady=5, padx=5)
#---------------------------------------------------------------
miFrame1 = Frame(root)
miFrame1.pack()
#------- Label y entry,s Código producto -----------------------
lCodigo = Label(miFrame1, text='Cod_Prod')
lCodigo.grid(row=4, column=0,sticky='e', pady=5, padx=5)
tCodigo1 = Entry(miFrame1, width=7)
tCodigo1.grid(row=5, column=0, pady=5, padx=5)
tCodigo2 = Entry(miFrame1, width=7)
tCodigo2.grid(row=6, column=0, pady=5, padx=5)
tCodigo3 = Entry(miFrame1, width=7)
tCodigo3.grid(row=7, column=0, pady=5, padx=5)
#------- Label y entry,s Descripción ---------------------------
lDes = Label(miFrame1, text='Descripción')
lDes.grid(row=4, column=1,sticky='ew', pady=5, padx=5)
tDes1 = Entry(miFrame1, width=7, state="readonly")
tDes1.grid(row=5, column=1, pady=5, padx=5)
tDes2 = Entry(miFrame1, width=7, state="readonly")
tDes2.grid(row=6, column=1, pady=5, padx=5)
tDes3 = Entry(miFrame1, width=7, state="readonly")
tDes3.grid(row=7, column=1, pady=5, padx=5)
#------- Label y entry,s Unidad --------------------------------
lUni = Label(miFrame1, text='Unidad')
lUni.grid(row=4, column=2,sticky='ew', pady=5, padx=5)
tUni1 = Entry(miFrame1, width=7, state="readonly")
tUni1.grid(row=5, column=2, pady=5, padx=5)
tUni2 = Entry(miFrame1, width=7, state="readonly")#width número de caracteres
tUni2.grid(row=6, column=2, pady=5, padx=5)
tUni3 = Entry(miFrame1, width=7, state="readonly")
tUni3.grid(row=7, column=2, pady=5, padx=5)
#------- Label y entry,s Cantidad ------------------------------
lCantidad = Label(miFrame1, text='Cantidad')
lCantidad.grid(row=4, column=3,sticky='ew', pady=5, padx=5)
tCantidad1 = Entry(miFrame1, width=7)
tCantidad1.grid(row=5, column=3, pady=5, padx=5)
tCantidad2 = Entry(miFrame1, width=7)#width número de caracteres
tCantidad2.grid(row=6, column=3, pady=5, padx=5)
tCantidad3 = Entry(miFrame1, width=7)
tCantidad3.grid(row=7, column=3, pady=5, padx=5)
#------- Label y entry,s Precio --------------------------------
lPrecio = Label(miFrame1, text='Precio')
lPrecio.grid(row=4, column=4,sticky='ew', pady=5, padx=5)
tPrecio1 = Entry(miFrame1, width=7, state="readonly")
tPrecio1.grid(row=5, column=4, pady=5, padx=5)
tPrecio2 = Entry(miFrame1, width=7, state="readonly")#width número de caracteres
tPrecio2.grid(row=6, column=4, pady=5, padx=5)
tPrecio3 = Entry(miFrame1, width=7, state="readonly")
tPrecio3.grid(row=7, column=4, pady=5, padx=5)
#------- Label y entry,s Subtotal ------------------------------
lSubtotal = Label(miFrame1, text='Subtotal')
lSubtotal.grid(row=4, column=5,sticky='ew', pady=5, padx=5)
tSubtotal1 = Entry(miFrame1, width=7, state="readonly")
tSubtotal1.grid(row=5, column=5, pady=5, padx=5)
tSubtotal2 = Entry(miFrame1, width=7, state="readonly")#width número de caracteres
tSubtotal2.grid(row=6, column=5, pady=5, padx=5)
tSubtotal3 = Entry(miFrame1, width=7, state="readonly")
tSubtotal3.grid(row=7, column=5, pady=5, padx=5)
#------- Label y entry,s Total --------------------------------
lTotal = Label(miFrame1, text='Total')
lTotal.grid(row=7, column=6,sticky='ew', pady=5, padx=5)
tTotal = Entry(miFrame1, width=7, state="readonly")
tTotal.grid(row=7, column=7, pady=5, padx=5)
#------ Botón guardar -----------------------------------------
guardar=Button(miFrame1, text='Guradar')
guardar.grid(row=8, column=3, pady=5, padx=5)
 
root.mainloop()