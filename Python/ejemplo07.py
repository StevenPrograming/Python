#Ejemplo 01 - MANEJO DE EXCEPCIONES

"""try:

    num1=240

    num2=10

    print(num1/num2)

    print("Calculo realizado correctamente")

except ZeroDivisionError:

    print("No se puede dividir un numero entre 0")


print("Fin del programa")"""

"""salir = "no"

while salir != "si":

    try:

        num1=int(input("Ingrese un numero: "))

        num2=int(input("Ingrese un numero: "))

        suma=num1+num2

        print("La suma es",suma)

        salir = input("¿Desea salir? ")

    except ValueError:

        print("No se permite texto solo numero")

        salir = input("¿Desea salir? ")

print("Gracias por usar el programa")"""

"""import re
 re
frase="Bienvenidos al 2020 ya termino el 2019"

buscar=re.findall(r'\d\d\d',frase)


print(buscar)"""

#Ejemplo 02
"""import re
patron=re.compile(r"\ben\b")
frase="enBienvenidos al año 2020 ya termino el 2019"
print(patron.match(frase))"""

#Ejemplo de validacion con regex
"""import re
frase="Hola como estan"
if re.compile("^[1-9]{1,8}$").match(frase):
    print("SI MATCH")
else:
    print("NO MATCH")"""

#import re
"""patron=re.compile(r"\ben\b")
frase="en Bienvenidos al en año 2020 ya termino en el 2019"
print(patron.search(frase))"""

"""patron=re.compile(r"\ben\b")
frase="en Bienvenidos al en año 2020 ya termino en el 2019"
print(patron.findall(frase))"""

"""patron=re.compile(r"\ben\b")
frase="en Bienvenidos al en año 2020 ya termino en el 2019"
#print(patron.finditer(frase))
for x in patron.finditer(frase):
    print(x)"""