import io

#Ejemplo 01 Escritura de archivo de texto:
#texto="Mi primera linea de texto\nMi segunda linea de texto"
"""texto="Mi primera linea de texto\nMi segunda linea de texto\nMi tercera linea de codigo"

archivo=open("archivo.txt","w")
archivo.write(texto)
archivo.close()"""

#Ejemplo 02 Lectura de archivo de texto
"""archivo=open("archivo.txt","r")
texto=archivo.read()
archivo.close()
print(texto)"""

#Ejemplo 03 Lectura de archivo de texto
"""archivo=open("archivo.txt","r")
lista=archivo.readlines()
archivo.close()
print(lista)"""

#Ejemplo 04 Lectura de archivo de texto
"""with open("archivo.txt","r") as archivo:
    for linea in archivo:
        print(linea)"""

#Ejemplo 05 Extension de archivo de texto(Agregar)
"""archivo=open("archivo.txt","a")
archivo.write("\nMi cuarta linea de codigo")
archivo.close()"""

"""archivo=open("archivo_temporal.txt","a")
archivo.close()"""

#Ejemplo 06 Puntero en archivo texto
"""archivo=open("archivo.txt","r")
archivo.seek(0)
texto=archivo.read(12)
archivo.close
print(texto)"""

#,"r+" el + se utiliza para hacer ambas cosas
#len tamaño de caracteres
#readline lee una linea
#siempre que se cuenta los caracteres se empieza de cero 0

#Ejemplo 07 Puntero en archivo texto
"""archivo=open("archivo.txt","r")
archivo.seek(0)
archivo.seek(len(archivo.readline())) #abajo
#archivo.seek(25)
texto=archivo.read()
archivo.close()
print(texto)"""

#Ejemplo 08 Puntero en archivo texto
"""archivo=open("archivo.txt","r+")
lista=archivo.readlines()
lista[2]="esta linea se ha modificado\n"
archivo.seek(0)
archivo.writelines(lista)
archivo.close()"""
