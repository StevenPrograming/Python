"""num1=int(input("Ingrese el primer valor: "))
num2=int(input("Ingrese el segundo valor: "))
if num1>num2:
    aux=num2
    num2=num1
    num1=aux
print("El primer numero es",num1)
print("El segundo numero es",num2)""" 

#While
"""numero=int(input("Ingresa un numero positivo: "))
while(numero<0):
    print("El numero es incorrecto!!")
    numero=int(input("Ingresa un numero positivo: "))
print("Gracias por la informacion")"""

#ejercicio while
"""contador=1
while contador<6:
    print("Steven")
    contador=contador+1"""

#for(range)
"""veces=int(input("¿Cuantas veces quiere te salude?: "))
for i in range(veces):
    print(f"{i+1} - Hola")
print("Fin del saludo")"""

#For(list)
"""lista=["enero","febrero","marzo","abril","mayo"]
for i in lista:
    print(i)
print("fin del algoritmo")"""

#for(cadena)
"""for i in "SENATI":
    print("ya tengo la: ",i)
print("fin del algoritmo")"""

#bucle anidado
"""for i in range(3):  
    for j in range(2):
        print(f"Padre posicion: {i+1} Hijo: {j+1}")"""

#Caso propuesto tabla de multiplicar
"""for i in range(12): #padre siempre espera a hijo
    for j in range(12): 
        print(f"{i+1}x{j+1} = {(i+1)*(j+1)}")"""

#Caso propuesto suma y promedio con bucle
"""valor=0
for i in range(5):
    num=int(input("Ingresa valor: "))
    valor=valor+num
print("Su suma es",valor)
valor=valor/5
print("Su promedio es",valor)"""

#ordenar 3 numeros
"""num1=34 
num2=56
num3=12
aux=0
for i in range(3):
    if num1>num2:
        aux=num1#34
        num1=num2#56
        num2=aux#34
    if num2>num3:
        aux=num2#56
        num2=num3#12
        num3=aux#56
print(num1)
print(num2)
print(num3)"""
