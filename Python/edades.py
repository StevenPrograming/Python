print("===================BIENVENIDO A LA SALA DE JUEGOS===================")
print("                =====>INGRESE SU INFORMACION<=====")
nombre=input("¿Cual es tu nombre?: ")
edad=int(input("¿Que edad tiene?: "))

if edad < 0:
    print("No se puede tener una edad negativa")
if edad >= 0 and edad <= 4:
    print("Es usted menor de edad puede entrar gratis")
if edad >= 5 and edad <= 14:
    print("Debe pagar S/10 para entrar")
else:
    print("Debe pagar S/15 para entrar")