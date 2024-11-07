"""class Saludo:

    def __init__(self, nombre, apellidos):
      self.nombre = nombre
      self.apellidos = apellidos

    def saludar(self):
        print(f"Hola soy {self.nombre} {self.apellidos} saludos")

objeto = Saludo("Edgar","Roncal")
objeto.saludar()"""

"""import re
class Tarjeta:

    def __init__(self, num):
      self.tarjeta = num
    
    def validarvisa(self):
        if re.compile("^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$").match(self.tarjeta):
            print("Tarjeta Visa Valida")
        else:
            print("Tarjeta Visa no valida")
    
    def validarmastercard(self):
        if re.compile("^[0-9]{5}-[0-9]{5}-[0-9]{5}-[0-9]{5}$").match(self.tarjeta):
            print("Tarjeta MasterCard Valida")
        else:
            print("Tarjeta MasterCard no valida")


print("¿Que tarjeta utiliza?")
tarjeta = input("Visa o Mastercard: ")
if tarjeta=="Visa":
    num1 = input("Coloque su numero de tarjeta y separelo por guiones: ")
    visa = Tarjeta(num1)
    visa.validarvisa()
elif tarjeta=="Mastercard":
    num2 = input("Coloque su numero de tarjeta y separelo por guiones: ")
    mastercard = Tarjeta(num2)
    mastercard.validarmastercard()
else:
    print("No valido")"""