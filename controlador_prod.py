# Esta es la interfase que armamos para e usuario

import Modelo


def ListarProducto(): #funciona
    com = Modelo.Conectar()

    listado = com.ListarProducto()

    print("\n! ID PRODUCTO  !  NOMBRE PRODUCTO  !  STOCK  !  PRECIO  !  UNIDAD DE MEDIDA  !  RECETA")

    for Producto in listado:
        print("  ",Producto[0],"\t\t",Producto[1],"\t\t",str(Producto[2])+"\t\t$"+str(Producto[3]),"\t\t",Producto[4],"\t\t",Producto[5]) #falta comleetar el print
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


def InsertarProducto():
    con = Modelo.Conectar()

    nombre_Poducto = input("\nIngrese el nombre del Producto: ")
    stock = int(input("\nIngrese el stock del Producto: "))
    precio= int(input("\nIngrese el precio del Producto: "))
    unidad_de_medida= input("\nIngrese la unidad de medida del Producto: ")

    #Aquí deberían brindarle la posibilidad al usuario de elegir una receta existente 
    # en la BD o que cree una receta nueva.

    nuevoProducto= Modelo.Producto(0,nombre_Poducto,stock,precio,unidad_de_medida,0)

    con.InsertarProducto(nuevoProducto)
    input("Para continuar presione enter")


