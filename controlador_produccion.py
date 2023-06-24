import Modelo


def Borrar_Produccion(): #FUNCIONA
    com = Modelo.Conectar()
    condicion = (input("el numero de registro de produccion a eliminar: "))
    com.DeleteProduccion(condicion)

def Listar_Produccion(): #FUNCIONA
    
    com = Modelo.Conectar()

    listado = com.ListarProduccion()

    print("\n! ID PRODUCCION  !  FECHA  !  NUMERO DE PEDIDO  !  PRODUCTO PEDIDO  !  CANTIDAD PEDIDA  !  UNIDAD")

    for produccion in listado:
        print("  ",produccion[0],"\t\t",str(produccion[1]),"\t\t",produccion[2],"\t\t$",str(produccion[3]),"\t\t",produccion[4],"\t\t",str(produccion[5])) #falta comleetar el print
        input("Para continuar presione enter")

def Actualizar_Produccion(): #FUNCIONA
    con = Modelo.Conectar()

    con.UpdateProduccion()

def Insertar_Produccion(): #FUNCIONA
    
    
    iD_produccion = input("Ingrese el ID de la produccion: ")
    fecha = str(input("Ingrese fecha del pedido: "))
    num_pedido = int(input("Ingrese numero del pedido: "))
    prod_pedido = str(input("Ingrese el producto pedido: "))
    cantidad_pedida = int(input("Ingrese la cantidad pedida: "))
    unidad = str(input("Ingrese unidad del producto: "))

    produccion = Modelo.Produccion(iD_produccion,fecha,num_pedido,prod_pedido,cantidad_pedida,unidad)

    Con = Modelo.Conectar()
    Con.InsertarProduccion(produccion)
    
 

#Borrar_Produccion() - funciona

#Listar_Produccion() - funciona

#Actualizar_Produccion() - funciona

#Insertar_Produccion() - funciona