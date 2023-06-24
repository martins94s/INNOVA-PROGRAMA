import Modelo


def Listar_Insumo(): #funciona
    com = Modelo.Conectar()

    listado = com.ListarInsumo()

    print("\n! ID INSUMO  !  NOMBRE   !  CANTIDAD  !  UNIDAD RECETA")

    for insumo in listado:
        print("  ",insumo[0],"\t\t",insumo[1],"\t\t",insumo[2],"\t\t",(insumo[3])) 
        input("Para continuar presione enter")

def Borrar_Insumo(): #funciona
    com = Modelo.Conectar()
    condicion = (input("el numro de insumo a eliminar: "))
    com.DeleteInsumo(condicion)

def Insertar_Insumo(): #funciona
    com = Modelo.Conectar()

    iD_insumo = int(input("ingrese el ID del insumo: "))
    nombre = str(input("ingrese nombre del insumo: "))
    cantidad = int(input("ingrese cantidad del insumo: "))
    insumo_unidad = str(input("ingrese unidad del insumo: "))

    insumo = Modelo.Insumo(iD_insumo,nombre,cantidad,insumo_unidad)

    com.InsertarInsumo(insumo)

def Actualizar_Insumo(): #funciona
    con = Modelo.Conectar()

    con.UpdateInsumo()




#Listar_Insumo() - FUNCIONA

#Borrar_Insumo() - FUNCIONA
#Insertar_Insumo() - FUNCIONA

#Actualizar_Insumo() - Funciona