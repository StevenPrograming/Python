#import pymysql

#Caso 1 Consultar una tabla de una BD
"""conexion=pymysql.connect(host='localhost',user='root',password='',db='senati_bd')
cur=conexion.cursor()
cur.execute("SELECT * FROM cursos")
for id_curso, nombre_curso in cur.fetchall():
    print(id_curso,nombre_curso)
conexion.close()"""

#Caso traer los datos de la tabla alumno
"""conexion=pymysql.connect(host='localhost',user='root',password='',db='senati_bd')
cur=conexion.cursor()
cur.execute("SELECT * FROM alumno")
for id_alumno, nombres, apellidos, carrera in cur.fetchall():
    print(id_alumno, nombres, apellidos, carrera)
conexion.close()"""

#Ahora con input
"""print("Aqui es tan los codigos que utilizara\nMAT001\nCON001\nINF001")
salir = "no"
while salir != "si":
    codigo = input("Coloque el codigo del curso: ")
    conexion=pymysql.connect(host='localhost',user='root',password='',db='senati_bd')
    cur=conexion.cursor()
    if codigo == "CON001":
        cur.execute("SELECT * FROM cursos WHERE id_curso = 'CON001'")
        for id_curso, nombre_curso in cur.fetchall():
            print(id_curso,nombre_curso)
    elif codigo == "MAT001":
        cur.execute("SELECT * FROM cursos WHERE id_curso = 'MAT001'")
        for id_curso, nombre_curso in cur.fetchall():
            print(id_curso,nombre_curso)
    elif codigo == "INF001":
        cur.execute("SELECT * FROM cursos WHERE id_curso = 'INF001'")
        for id_curso, nombre_curso in cur.fetchall():
            print(id_curso,nombre_curso)
    conexion.close()
    salir = input("¿Desea salir?: ")
print('Gracias por usar el programa')"""


"""conexion=pymysql.connect(host='localhost',user='root',password='',db='senati_bd')
cur=conexion.cursor()
respuesta=cur.execute("INSERT INTO cursos VALUES ('INF100','DESARROLLO WEB')")
conexion.commit()
if respuesta:
    print("Se ha insertado el registro")
else:
    print("Operacion fallida")
conexion.close()"""


"""codigo=input("Ingresa el codigo del curso: ")
nombre=input("Ingresa el nombre del curso: ")
conexion=pymysql.connect(host='localhost',user='root',password='',db='senati_bd')
cur=conexion.cursor()
respuesta=cur.execute(f"INSERT INTO cursos VALUES ('{codigo}','{nombre}')")
conexion.commit()
if respuesta:
    print("Se ha insertado el registro")
else:
    print("Operacion fallida")
conexion.close()"""