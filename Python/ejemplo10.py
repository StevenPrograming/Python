"""import csv
contactos = [
    ("Edgar", "Desarrollador Web", "edgar@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

with open("contactos.csv","w",newline="\n") as csvfile:
    writer=csv.writer(csvfile,delimiter=",")
    for contacto in contactos:
        writer.writerow(contacto)"""

"""import json
contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]
datos = []
for nombre, empleo, email in contactos:
    datos.append({"nombre":nombre, "empleo":empleo, "email":email})
with open("contactos.json", "w") as jsonfile:
    json.dump(datos, jsonfile)"""