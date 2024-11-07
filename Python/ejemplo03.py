#generador de correo
"""print("Hola vamos hacer un generador de correo empresarial con la siguiente informacion")
prinombre=input("¿Cual es tu primer nombre?: ")
priapellido=input("¿Cual es tu primer apellido?: ")
segunapellido=input("¿Cual es tu segundo apellido?: ")
año=input("¿Cual es tu año de nacimiento?: ")
correo=input("¿Cual es el correo empresarial?: ")
subcadena=prinombre[:1]
subcadena2=segunapellido[:1]
subcadena3=año[2:4]
subcadena4=correo[4:]
generador=subcadena+priapellido+subcadena2+subcadena3+"@"+subcadena4
print("Bien tu correo empresarial es",generador)"""

#ejemplo de condicional
"""numero=int(input("Escriba un numero positivo: "))
if numero < 0:
    print("No coloques un numero negativo")
print(f"Usted a ingresado el numero {numero}")"""

#ejemplo de sentencia condicional anidada
"""nota=int(input("Ingresa una calificacion: "))
if nota>16:
    print("Eres un alumno bueno")
else:
    if nota>12:
        print("Eres un alumno regular")
    else:
        print("Eres un alumno malo")"""

#ejemplo de condicional else if
"""edad=int(input("Ingresa tu edad: "))
if edad<0:
    print("No puedes ingresar un valor negativo")
elif edad<18:
    print("Tu eres menor de edad")
else:
    print("Tu eres mayor de edad")"""

#Caso propuesto
"""name=input("¿Cual es su nombre?: ")
nota=int(input("¿Cual es su calificacion?: "))
if nota>17:
    print(name,"es un alumno excelente")
elif nota>15:
    print(name,"es un alumno bueno")
elif nota>12:
    print(name,"es un alumno regular")
elif nota>8:
    print(name,"es un alumno malo")
else:
    print(name,"es un alumno pesimo")"""

#Caso propuesto 2
"""edad=int(input("¿Cual es tu edad?: "))
if edad>=5 and edad<=13:
    print("Estas en la etapa de la niñez")
elif edad>=14 and edad<=17:
    print("Estas en la etapa de la adolescencia")
elif edad>=18 and edad<=35:
    print("Estas en la etapa de los adultos jovenes")
elif edad>=36 and edad<=64:
    print("Estas en la etapa de la adultez")
else:
    print("Estas en la etapa de la tercera edad")"""

#Caso propuesto 3
"""num1=int(input("Deme un numero: "))
num2=int(input("Deme otro numero:"))
if num1>num2:
    print("El numero",num1,"es el mayor")
    print("El numero",num2,"es el menor")
else:
    print("El numero",num1,"es el menor")
    print("El numero",num2,"es el mayor")"""