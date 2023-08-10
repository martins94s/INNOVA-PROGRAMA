import mysql.connector
from mysql.connector import Error


class Conectar():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = '3308', 
                user = 'root', 
                password ='', 
                db= 'big_bread'
            )
            if self.conexion.is_connected():
                print("")
                print("LA CONEXION ES EXITOSA")
                print("")
                
        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")

#******************************************PRODCUTO**************************************************
    def ListarProducto(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "SELECT * FROM Producto"
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)
    
    def InsertarProducto(self,producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT into Producto values(null,%s,%s,%s,%s,null)"

                data = (producto.getnombre_Producto(),
                        producto.getstock(),
                        producto.getprecio(),
                        producto.getunidad_de_medida()
                        )

                cursor.execute(sentenciaSQL,data)

                self.conexion.commit()
                self.conexion.close()
                print("Producto insertado correctamente")

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)

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

#************************************************RECETA******************************************************
def ListarReceta(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "SELECT * FROM Receta"
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)

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

def InsertarReceta(self,receta):
        if self.conexion.is_connected():
            try:
                mi_cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT into receta values(null,%s,%s,%s,%s)"

                data = (

                        receta.getid_receta(),
                        receta.getnombre_receta(),
                        receta.getdescrip_receta(),
                        receta.cantidad_por_rec(),
                        receta.getunidad_rec()
                        
                        )

                mi_cursor.execute(sentenciaSQL,data)

                self.conexion.commit()
                self.conexion.close()
                print("Receta insertado correctamente")

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)
        

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


#************************************************INSUMO******************************************************
def ListarInsumo(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "SELECT * FROM Insumo"
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)


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

def InsertarInsumo(self,insumo): # FUNCIONA - INSERTAR UN PRODUCTO EN UNA TABLA EN UNA BASE DE DATOS EN MYSQL - 9
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT into insumo values(null,%s,%s,%s)"

                data = (insumo.getnombre_Producto(),
                        insumo.getstock(),
                        insumo.getprecio(),
                        insumo.getunidad_de_medida()
                        )

                cursor.execute(sentenciaSQL,data)

                self.conexion.commit()
                self.conexion.close()
                print("insumo insertado correctamente")

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)

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
def ListarProduccion(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "SELECT * FROM Produccion"
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)

def DeletePoduccion(self): # FUNCIONA - BORRAR REGISTRO DE PRODUCCION 
        if self.conexion.is_connected():
            try:
                mi_cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM produccion WHERE iD_produccion = "
                mi_cursor.execute(sentenciaSQL)
                self.conexion.commit()
                print("El registro de la produccion se ha eliminado")
                       
            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)

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
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT into producccion values(null,%s,%s,%s,%s,%s)"

                data = (produccion.getnombre_Producto(),
                        produccion.getstock(),
                        produccion.getprecio(),
                        produccion.getunidad_de_medida()
                        )

                cursor.execute(sentenciaSQL,data)

                self.conexion.commit()
                self.conexion.close()
                print("Produccion insertado correctamente")

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)




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




