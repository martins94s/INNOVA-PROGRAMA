import mysql.connector

from producto_bd import Producto


class Conectar():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = input("Ingrese el Puerto: "), # 3306
                user = input("Ingrese el Usuario: "), # root
                password = input("Ingrese el Password: "),# " " - vacio + enter
                db= input("Ingrese el nombre de la Base de Datos: ")
            )
            if self.conexion.is_connected():
                print("")
                print("LA CONEXION ES EXITOSA")
                print("")
                
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")


    def traer_db(self):   # MUESTRA EL LISTADO DE BASES EN MYSQL - 1     
        try:
            if self.conexion.is_connected():
                print("esta conectado")       
                mi_cursor = self.conexion.cursor()
                print("Para mostrar el listado de bases de datos")
                query = str(input("Ingrese la sentencia en mayuscula:")) # SHOW DATABASES
                mi_cursor.execute(query)
                for db in mi_cursor:
                    print (db)
            
                mi_cursor.close()
                self.conexion.close()          
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS") 

    def crear_db(self): #CREA UNA BASE DE DATOS EN MYSQL - 2
        try:
            if self.conexion.is_connected():
                print("esta conectado")       
                mi_cursor = self.conexion.cursor()
                print("Para crear un BD en el listado de bases de datos")
                query = str(input("Ingrese la sentencia en mayuscula:")) # SHOW DATABASES
                mi_cursor.execute(query)           
                mi_cursor.close()
                self.conexion.close()
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")  


    def eliminar_db(self): # ELIMINIA UNA BASE DE DATOS EN MYSQL - 3
        try:
            if self.conexion.is_connected():
                print("esta conectado")       
                mi_cursor = self.conexion.cursor()
                print("Para eliminar un BD en el listado de bases de datos")
                query = str(input("Ingrese la sentencia en mayuscula:")) # DROP DATABASE *****
                mi_cursor.execute(query)           
                mi_cursor.close()
                self.conexion.close()
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS") 

    def ver_tb_db(self): # PERMITE VER LAS TABLAS DE UNA BASE DE DATOS DE MYSQL - 4
        try:
            if self.conexion.is_connected():
                mi_cursor = self.conexion.cursor()
                print("Para mostrar una tabla en la base de datos")
                query = str(input("Ingrese la sentencia en mayuscula:")) #SHOW TABLES
                mi_cursor.execute(query)

                for datos in mi_cursor:
                    print(datos)

                mi_cursor.close()
                self.conexion.close()
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS") 

    def crear_tb_db(self): # CREA UNA TABLA EN UNA BASE DE DATOS EN MYSQL - 5
        try:
            if self.conexion.is_connected():
                mi_cursor = self.conexion.cursor()
                print("Para crear una tabla en la base de datos")
                query = str(input("Ingrese la sentencia en mayuscula:")) #CREATE TABLE *****(*** int, **** VARCHAR(20))
                mi_cursor.execute(query)

                mi_cursor.close()
                self.conexion.close()
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS") 


    def eliminar_tb_db(self): # ELIMINAR UNA TABLA EN UNA BASE DE DATOS EN MYSQL - 6
        try:
            if self.conexion.is_connected():
                mi_cursor = self.conexion.cursor()
                print("Para eliminar una tabla en la base de datos")
                query = str(input("Ingrese la sentencia en mayuscula:")) # DROP TABLE ****
                mi_cursor.execute(query)

                mi_cursor.close()
                self.conexion.close()
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")


    def insertar_insumo_tb(self,iD_insumo,nombre,cantidad,insumo_unidad): 
        # INSERTAR UN INSUMO EN UNA TABLA EN UNA BASE DE DATOS EN MYSQL - 7
        try:
            if self.conexion.is_connected():
                mi_cursor = self.conexion.cursor()
                #query = "INSERT INTO insumo(iD_insumo,nomnbre,cantidad,insumo_unidad) VALUES(%s, %s, %s, %s)"
                #query = str(input("Ingrese la sentencia en mayuscula:"))
                query = "INSERT INTO insumo(iD_insumo,nombre,cantidad,insumo_unidad) VALUES (%s, %s,%s, %s)"
                valores = (iD_insumo,nombre,cantidad,insumo_unidad)
                mi_cursor.execute(query,valores)
                self.conexion.commit()
                print("Insumo insertado correctamente")
                
                mi_cursor.close()
                
                print(iD_insumo)
                print(nombre)
                print(cantidad)
                print(insumo_unidad)

                self.conexion.close()
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")


    def ver_insumos_tb(self): # VER UN INSUMO EN UNA TABLA EN UNA BASE DE DATOS EN MYSQL - 8
        try:
            if self.conexion.is_connected():
                mi_cursor = self.conexion.cursor()
                #print("Para ver datos una tabla en la base de datos")
                query = str(input("Ingrese la sentencia en mayuscula:")) #SELECT * FROM Productos
                mi_cursor.execute(query)
                resultados= mi_cursor.fetchall()
                mi_cursor.close()
                return resultados
                self.conexion.close()
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")


    def insertar_producto_tb(self,iD_Producto,nombre_Producto,stock,precio,unidad_de_medida,iD_Receta): 
        # INSERTAR UN PRODUCTO EN UNA TABLA EN UNA BASE DE DATOS EN MYSQL - 9
        try:
            if self.conexion.is_connected():
                mi_cursor = self.conexion.cursor()
                #query = "INSERT INTO insumo(iD_insumo,nomnbre,cantidad,insumo_unidad) VALUES(%s, %s, %s, %s)"
                #query = str(input("Ingrese la sentencia en mayuscula:"))
                query = "INSERT INTO producto(iD_Producto,nombre_Producto,stock,precio,unidad_de_medida,iD_Receta) VALUES (%s, %s, %s, %s, %s, %s)"
                valores = (iD_Producto,nombre_Producto,stock,precio,unidad_de_medida,iD_Receta)
                mi_cursor.execute(query,valores)
                self.conexion.commit()
                print("Producto insertado correctamente")
                
                mi_cursor.close()

                self.conexion.close()
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")


    def ver_producto_tb(self): # VER UN PRODUCTO EN UNA TABLA EN UNA BASE DE DATOS EN MYSQL - 10
        try:
            if self.conexion.is_connected():
                mi_cursor = self.conexion.cursor()
                print("Informacion de los  productos")
                #query = str(input("Ingrese la sentencia en mayuscula:")) #SELECT * FROM Productos
                query = "SELECT * FROM producto"
                mi_cursor.execute(query)
                resultados= mi_cursor.fetchall()
                mi_cursor.close()
                return resultados
                self.conexion.close()
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")
    



##############################################################################################

print("")
print("")
print("***********************************************************")
print("******* Bienvenidos a la Base de Datos de Big Bread *******")
print("***********************************************************")
print("")
print("Para acceder debera ingresar su Usuario y Password y elegir una Base de Datos")
tor = Conectar()
print("Desea realizar una consulta?")
eleccion = str(input("Ingrese -y- en caso afirmativo o -n- en caso negativo: "))
if eleccion == "y":
    print("")
    print("Seleccione una opcion: ")
    print("1 - Ver bases de datos")
    print("2 - Crear una BD")
    print("3 - Eliminar un BD")
    print("4 - Ver tablas en BD")
    print("5 - Crear tabla en BD")
    print("6 - Eliminar tabla en BD")
    print("7 - Insertar insumo en Tabla")
    print("8 - Listado de insumos")

