# este metodo es para ir a la base de datos a uscar los datos
import mysql.connector
from mysql.connector import Error

class Conectar():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = "3306", # 3306
                user = "root", # root
                password = "",# " " - vacio + enter
                db= "big_bread"
            )
            if self.conexion.is_connected():
                print("")
                print("LA CONEXION ES EXITOSA")
                print("")
                
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")

   
    # *********************************************** PRODUCTOS ********************************************
    def InsertarProducto(self,producto): # FUNCIONA - INSERTAR UN PRODUCTO EN UNA TABLA EN UNA BASE DE DATOS EN MYSQL - 9
        
        if self.conexion.is_connected(): 
            try:   
                mi_cursor = self.conexion.cursor()
                #query = "INSERT INTO productos (iD_Producto,nombre_Producto,stock,precio,unidad_de_medida,iD_Receta) VALUES "
                #query = str(input("Ingrese la sentencia en mayuscula:"))
                query = "INSERT INTO producto(iD_Producto,nombre_Producto,stock,precio,unidad_de_medida,iD_Receta) VALUES (%s, %s, %s, %s, %s, %s)"
                data = (producto.getiD_Producto(),
                        producto.getnombre_Producto(),
                        producto.getstock(),
                        producto.getprecio(),
                        producto.getunidad_de_medida(),
                        producto.getiD_Receta()
                        )
                mi_cursor.execute(query,data)
                self.conexion.commit()
                print("Producto insertado correctamente")
                mi_cursor.close()
                self.conexion.close()
            except Error as e:
                print("Se produjo un Error: ",e)  

    def ListarProductos(self): # FUNCIONA - SELECCIONAR UN PRODUCTO EN UNA TABLA EN UNA BASE DE DATOS EN MYSQL - 10
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
        except Error as e:
            print("Se produjo un Error: ",e)   

    def UpdateProducto(self): #FUNCIONA
        if self.conexion.is_connected():
            try:
                mi_cursor = self.conexion.cursor()
                condicion = input("Ingrese lo que desee actualizar; ")
                query = "UPDATE producto SET "
                mi_cursor.execute(query+condicion)
                self.conexion.commit()
                print("Producto actualizado correctamente")
                mi_cursor.close()
                self.conexion.close()
            except:
                print("NO SE PUDO CONETAR A LA BASE DE DATOS")

    def DeleteProducto(self,condicion): # FUNCIONA - BORRAR UN PRODUCTO - 
        if self.conexion.is_connected():
            try:
                mi_cursor = self.conexion.cursor()
                query = "DELETE FROM producto WHERE iD_producto = "
                cond = str(condicion)
                mi_cursor.execute(query+cond)
                self.conexion.commit()
                print("El Producto se ha eliminado")
                       
            except Error as e:
                print("Se produjo un Error: ",e)

    # *********************************************** RECETAS ***********************************************

    def ListarReceta(self): # FUNCIONA - LISTAR LAS FRECETAS - 
        try:
            if self.conexion.is_connected():
                mi_cursor = self.conexion.cursor()
                query = "SELECT * FROM receta"
                mi_cursor.execute(query)
                resultados= mi_cursor.fetchall()
                mi_cursor.close()
                return resultados
                self.conexion.close()
        except Error as e:
            print("Se produjo un Error: ",e)  

    def DeleteReceta(self,condicion): # FUNCIONA - BORRAR UN RECETA - Funciona
        if self.conexion.is_connected():
            try:
                mi_cursor = self.conexion.cursor()
                query = "DELETE FROM receta WHERE iD_receta = "
                cond = str(condicion)
                mi_cursor.execute(query+cond)
                self.conexion.commit()
                print("La receta se ha eliminado")
                       
            except Error as e:
                print("Se produjo un Error: ",e)   

    def InsertarReceta(self,receta): # FUNCIONA - INSERTAR UN receta EN UNA TABLA EN UNA BASE DE DATOS EN MYSQL - 9
        
        if self.conexion.is_connected(): 
            try:   
                mi_cursor = self.conexion.cursor()
                query = "INSERT INTO receta (iD_receta,nombre_receta,descrip_receta,cantidad_por_receta,unidad_rec) VALUES (%s, %s, %s, %s, %s)"
                data = (receta.getiD_receta(),
                        receta.getnombre_receta(),
                        receta.getdescrip_receta(),
                        receta.getcantidad_por_receta(),
                        receta.getunidad_rec()
                        )
                mi_cursor.execute(query,data)
                self.conexion.commit()
                print("Insumo insertado correctamente")
                mi_cursor.close()
                self.conexion.close()
            except Error as e:
                print("Se produjo un Error: ",e)  

    def UpdateReceta(self): 

        if self.conexion.is_connected():
            try:
                mi_cursor = self.conexion.cursor()
                condicion = str(input("Ingrese lo que desee actualizar de la receta; "))
                query = "UPDATE receta SET "
                mi_cursor.execute(query+condicion)
                self.conexion.commit()
                print("receta actualizada correctamente")
                mi_cursor.close()
                self.conexion.close()
            except:
                print("NO SE PUDO CONETAR A LA BASE DE DATOS")


    # ********************************************** INSUMOS **************************************************
    def ListarInsumo(self):  # FUNCIONA- LISTAR INSUMOS - 
        if self.conexion.is_connected():
            try:
                mi_cursor = self.conexion.cursor()
                query = "SELECT * FROM insumo"
                mi_cursor.execute(query)
                resultados= mi_cursor.fetchall()
                mi_cursor.close()
                return resultados
                self.conexion.close()
            except Error as e:
                print("Se produjo un Error: ",e)  

    def DeleteInsumo(self,condicion): # FUNCIONA - BORRAR UN RECETA - Funciona
        if self.conexion.is_connected():
            try:
                mi_cursor = self.conexion.cursor()
                query = "DELETE FROM insumo WHERE iD_insumo = "
                cond = str(condicion)
                mi_cursor.execute(query+cond)
                self.conexion.commit()
                print("El insumo se ha eliminado")
                       
            except Error as e:
                print("Se produjo un Error: ",e) 

    def InsertarInsumo(self,insumo): # FUNCIONA - INSERTAR UN insumo EN UNA TABLA EN UNA BASE DE DATOS EN MYSQL - 9
        
        if self.conexion.is_connected(): 
            try:   
                mi_cursor = self.conexion.cursor()
                query = "INSERT INTO insumo (iD_insumo,nombre,cantidad,insumo_unidad) VALUES (%s, %s, %s, %s)"
                data = (insumo.getiD_insumo(),
                        insumo.getnombre(),
                        insumo.getcantidad(),
                        insumo.getinsumo_unidad(),
                        )
                mi_cursor.execute(query,data)
                self.conexion.commit()
                print("Insumo insertado correctamente")
                mi_cursor.close()
                self.conexion.close()
            except Error as e:
                print("Se produjo un Error: ",e)  

    def UpdateInsumo(self): # FUNCIONA
        if self.conexion.is_connected():
            try:
                mi_cursor = self.conexion.cursor()
                condicion = input("Ingrese lo que desee actualizar; ")
                query = "UPDATE insumo SET "
                mi_cursor.execute(query+condicion)
                self.conexion.commit()
                print("Insumo actualizado correctamente")
                mi_cursor.close()
                self.conexion.close()
            except:
                print("NO SE PUDO CONETAR A LA BASE DE DATOS")


# *********************************************** PRODUCCION ************************************************
    def ListarProduccion(self):  #FUNCIONA - LISTAR PRODUCCION - 
        if self.conexion.is_connected():
            try:
                mi_cursor = self.conexion.cursor()
                print("Informacion de la  produccion")
                query = "SELECT * FROM produccion"
                mi_cursor.execute(query)
                resultados= mi_cursor.fetchall()
                mi_cursor.close()
                return resultados
                self.conexion.close()
            except Error as e:
                print("Se produjo un Error: ",e) 

    def DeleteProduccion(self,condicion): # FUNCIONA - BORRAR REGISTRO DE PRODUCCION 
        if self.conexion.is_connected():
            try:
                mi_cursor = self.conexion.cursor()
                query = "DELETE FROM produccion WHERE iD_produccion = "
                cond = str(condicion)
                mi_cursor.execute(query+cond)
                self.conexion.commit()
                print("El registro de la produccion se ha eliminado")
                       
            except Error as e:
                print("Se produjo un Error: ",e) 

    def UpdateProduccion(self): # FUNCIONA
        if self.conexion.is_connected():
            try:
                mi_cursor = self.conexion.cursor()
                condicion = input("Ingrese lo que desee actualizar; ")
                query = "UPDATE produccion SET "
                mi_cursor.execute(query+condicion)
                self.conexion.commit()
                print("Produccion actualizada correctamente")
                mi_cursor.close()
                self.conexion.close()
            except:
                print("NO SE PUDO CONETAR A LA BASE DE DATOS")

    def InsertarProduccion(self,produccion): # FUNCIONA - INSERTAR UN PRODUCTO EN UNA TABLA EN UNA BASE DE DATOS EN MYSQL - 9
        
        if self.conexion.is_connected(): 
            try:   
                mi_cursor = self.conexion.cursor()
                query = "INSERT INTO produccion(iD_produccion,fecha,num_pedido,prod_pedido,cantidad_pedida,unidad) VALUES (%s, %s, %s, %s, %s, %s)"
                data = (produccion.getiD_produccion(),
                        produccion.getfecha(),
                        produccion.getnum_pedido(),
                        produccion.getprod_pedido(),
                        produccion.getcantidad_pedida(),
                        produccion.getunidad()
                        )
                mi_cursor.execute(query,data)
                self.conexion.commit()
                print("Produccion insertada correctamente")
                mi_cursor.close()
                self.conexion.close()
            except Error as e:
                print("Se produjo un Error: ",e) 

# ********************************************** CLASE PRODUCTO *********************************************
class Producto(): # FUNCIONA
    ID_Producto =0,
    Nombre_Producto = "",
    Stock =0,
    Precio = 0,
    Unidad_de_medida = "",
    ID_Receta = 0

    def __init__(self,iD_Producto,nombre_Producto,stock,precio,unidad_de_medida,iD_Receta):
        self.ID_Producto = iD_Producto 
        self.Nombre_Producto =nombre_Producto
        self.Stock = stock
        self.Precio = precio
        self.Unidad_de_medida = unidad_de_medida
        self.ID_Receta = iD_Receta
    
    def getiD_Producto(self): #el objetivo de este metodo es obtener el valor de este en especifico; ID_PRODUCTO
        return self.ID_Producto
    def getnombre_Producto(self):
        return self.Nombre_Producto
    def getstock(self):
        return self.Stock
    def getprecio(self):
        return self.Precio
    def getunidad_de_medida(self):
        return self.Unidad_de_medida
    def getiD_Receta(self):
        return self.ID_Receta
    
    def setiD_Producto(self,iD_Producto):# ESTE METODO ASIGNA UN VALOR A ESTE ATRIBUTO
        self.ID_Producto = iD_Producto
    def setnombre_Producto(self,nombre_Producto):
        self.Nombre_Producto = nombre_Producto
    def setstock(self,stock):
        self.Stock = stock
    def setprecio(self,precio):
        self.Precio = precio
    def setunidad_de_medida(self,unidad_de_medida):
        self.Unidad_de_medida = unidad_de_medida
    def setiD_Receta(self,iD_Receta):
        self.ID_Receta = iD_Receta  

# ********************************************** CLASE INSUMO ***********************************************

class Insumo(): # FUNCIONA 
    ID_Insumo =0,
    Nombre = "",
    Cantidad =0,
    Insumo_Unidad = ""

    def __init__(self,iD_insumo,nombre,cantidad,insumo_unidad):
        self.ID_Insumo = iD_insumo 
        self.Nombre = nombre
        self.Cantidad = cantidad
        self.Insumo_Unidad = insumo_unidad
    
    def getiD_insumo(self): #el objetivo de este metodo es obtener el valor de este en especifico; ID_PRODUCTO
        return self.ID_Insumo
    def getnombre(self):
        return self.Nombre
    def getcantidad(self):
        return self.Cantidad
    def getinsumo_unidad(self):
        return self.Insumo_Unidad
    
    def setiD_insumo(self,iD_insumo):# ESTE METODO ASIGNA UN VALOR A ESTE ATRIBUTO
        self.ID_Insumo = iD_insumo 
    def setnombre(self,nombre):
        self.Nombre = nombre
    def setcantidad(self,cantidad):
        self.Cantidad = cantidad
    def setinsumo_unidad(self,insumo_unidad):
        self.Insumo_Unidad = insumo_unidad
    
# ********************************************* CLASE RECETA *************************************************
class Receta(): #Funciona 
    ID_Receta = 0,
    Nombre_Receta = "",
    Descrip_Receta = "",
    Cantidad_Por_Receta = 0,
    Unidad_Rec = ""

    def __init__(self,iD_receta,nombre_receta,descrip_receta,cantidad_por_receta,unidad_rec):
        self.ID_Receta = iD_receta 
        self.Nombre_Receta = nombre_receta
        self.Descrip_Receta = descrip_receta
        self.Cantidad_Por_Receta = cantidad_por_receta
        self.Unidad_Rec = unidad_rec
    
    def getiD_receta(self): #el objetivo de este metodo es obtener el valor de este en especifico; ID_PRODUCTO
        return self.ID_Receta
    def getnombre_receta(self):
        return self.Nombre_Receta
    def getdescrip_receta(self):
        return self.Descrip_Receta
    def getcantidad_por_receta(self):
        return self.Cantidad_Por_Receta
    def getunidad_rec(self):
        return self.Unidad_Rec
    
    def setiD_receta(self,iD_receta):# ESTE METODO ASIGNA UN VALOR A ESTE ATRIBUTO
        self.ID_Receta = iD_receta 
    def setnombre_receta(self,nombre_receta):
        self.Nombre_Receta = nombre_receta
    def setdescrip_receta(self,descrip_receta):
        self.Descrip_Receta = descrip_receta
    def setcantidad_por_receta(self,cantidad_por_receta):
        self.Cantidad_Por_Receta = cantidad_por_receta
    def setunidad_rec(self,unidad_rec):
        self.Unidad_Rec = unidad_rec
    
# ********************************************* CLASE PRODUCCION *********************************************
class Produccion(): # 
    ID_Produccion =0,
    Fecha = "",
    Num_Pedido =0,
    Prod_Pedido = "",
    Cantidad_Pedida = 0,
    Unidad = ""

    def __init__(self,iD_produccion,fecha,num_pedido,prod_pedido,cantidad_pedida,unidad):
        self.ID_Produccion = iD_produccion
        self.Fecha = fecha
        self.Num_Pedido = num_pedido
        self.Prod_Pedido = prod_pedido
        self.Cantidad_Pedida = cantidad_pedida
        self.Unidad = unidad
    
    def getiD_produccion(self): #el objetivo de este metodo es obtener el valor de este en especifico; ID_PRODUCTO
        return self.ID_Produccion
    def getfecha(self):
        return self.Fecha
    def getnum_pedido(self):
        return self.Num_Pedido
    def getprod_pedido(self):
        return self.Prod_Pedido
    def getcantidad_pedida(self):
        return self.Cantidad_Pedida
    def getunidad(self):
        return self.Unidad
    
    def setiD_produccion(self,iD_produccion):# ESTE METODO ASIGNA UN VALOR A ESTE ATRIBUTO
        self.ID_Produccion = iD_produccion
    def setfecha(self,fecha):
        self.Fecha = fecha
    def setnum_pedido(self,num_pedido):
        self.Num_Pedido = num_pedido
    def setprod_pedido(self,prod_pedido):
        self.Prod_Pedido = prod_pedido
    def setcantidad_pedida(self,cantidad_pedida):
        self.Cantidad_Pedida = cantidad_pedida
    def setunidad(self,unidad):
        self.Unidad = unidad  


# ************************************* sector pruebas **********************************


""" esto funciona, no tirar ***** aqui se inserto un producto
iD_Producto = int(input("ingrese el ID del producto: "))
nombre_Producto = str(input("ingrese nombre propducto: "))
stock = int(input("ingrese stock: "))
precio = int(input("ingrese el precio: "))
unidad_de_medida = str(input("Ingrese la unidad de medida: "))
iD_Receta = int(input("ingrese la receta: "))

producto = Producto(iD_Producto, nombre_Producto, stock, precio, unidad_de_medida, iD_Receta)


Con = Conectar()
Con.InsertarProducto(producto)

"""
"""
#esto funciona, no tirar ***** aqui se inserto un insumo
iD_insumo = int(input("ingrese el ID del insumo: "))
nombre = str(input("ingrese nombre del insumo: "))
cantidad = int(input("ingrese cantidad del insumo: "))
insumo_unidad = str(input("ingrese unidad del insumo: "))


insumo = Insumo(iD_insumo, nombre, cantidad, insumo_unidad)


Con = Conectar()
Con.InsertarInsumo(insumo)
"""
"""
#esto funciona, no tirar ***** aqui se inserto una receta
iD_receta = int(input("Ingrese el ID de la receta: "))
nombre_receta = str(input("Ingrese nombre de la receta: "))
descrip_receta = str(input("Ingrese detalle de la receta: "))
cantidad_por_receta = int(input("Ingrese cantidad producida por la receta: "))
unidad_rec = str(input("Ingrese la unidad de  cantidad de la receta: "))


receta = Receta(iD_receta,nombre_receta,descrip_receta,cantidad_por_receta,unidad_rec)


Con = Conectar()
Con.InsertarReceta(receta)
"""
#condicion_1 = input("inserte el parametro : ")
#D_Producto = int(input("Indique el item ID: "))
"" 

#Con = Conectar()
#Con.UpdateProducto()

#Con = Conectar()
#Con.UpdateInsumo()

#Con = Conectar()
#Con.UpdateReceta()

#com = Conectar()
#condicion = input("ingrese la condicion:")
#com.DeleteProduccion(condicion)

#com = Conectar()
#com.ListarProduccion()

"""
iD_produccion = input("Ingrese el ID de la produccion: ")
fecha = str(input("Ingrese fecha del pedido: "))
num_pedido = int(input("Ingrese numero del pedido: "))
prod_pedido = str(input("Ingrese el producto pedido: "))
cantidad_pedida = int(input("Ingrese la cantidad pedida: "))
unidad = str(input("Ingrese unidad del producto: "))

produccion = Produccion(iD_produccion,fecha,num_pedido,prod_pedido,cantidad_pedida,unidad)

Con = Conectar()
Con.InsertarProduccion(produccion)

"""



