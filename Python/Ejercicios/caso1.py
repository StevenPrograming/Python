'''nombre=input("¿Cual es su nombre?: ")
edad=float(input("¿Cual es su edad?: "))

if (edad>=18):
    print (nombre, "es mayor de edad")
elif (edad<=0):
    print ("Esa edad no existe")
else:
    print (nombre, "es menor de edad")'''


factorial=1
print("Dame un numero")
x=eval (input())
for i in range (1, x+1):
    factorial=factorial*i
 
print(factorial)