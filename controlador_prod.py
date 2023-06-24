# Esta es la interfase que armamos para e usuario

import Modelo
from Modelo import Producto

def ListarProductos(): #funciona
    com = Modelo.Conectar()

    listado = com.ListarProductos()

    print("\n! ID PRODUCTO  !  NOMBRE PRODUCTO  !  STOCK  !  PRECIO  !  UNIDAD DE MEDIDA  !  RECETA")

    for producto in listado:
        print("  ",producto[0],"\t\t",producto[1],"\t\t",str(producto[2])+"\t\t$"+str(producto[3]),"\t\t",producto[4],"\t\t",producto[5]) #falta comleetar el print
        input("Para continuar presione enter")

def ActualizarProducto(): #funciona

    com = Modelo.Conectar()
    
    #condicion_1 = input("inserte el parametro : ")
    #iD_Producto = int(input("Indique el item ID: "))
    com.UpdateProducto()

def BorrarProducto(): #funciona
    com = Modelo.Conectar()
    condicion = (input("ingrese el item del producto: "))
    com.DeleteProducto(condicion)

def Insertar_Producto(): #funciona

    com = Modelo.Conectar()

    iD_Producto = int(input("ingrese el ID del producto: "))
    nombre_Producto = str(input("ingrese nombre propducto: "))
    stock = int(input("ingrese stock: "))
    precio = int(input("ingrese el precio: "))
    unidad_de_medida = str(input("Ingrese la unidad de medida: "))
    iD_Receta = int(input("ingrese la receta: "))

    producto = Producto(iD_Producto, nombre_Producto, stock, precio, unidad_de_medida, iD_Receta)

    com.InsertarProducto(producto)





#BorrarProducto() - #funciona
#ListarProductos() - #funciona
#Insertar_Producto() #- funciona

#ActualizarProducto()  #funciona