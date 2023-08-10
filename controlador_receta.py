import Modelo

def ListarReceta(): #funciona
    com = Modelo.Conectar()

    listado = com.ListarReceta()

    print("\n! ID RECETA  !  NOMBRE RECETA  !  DESCRIPCION RECETA  !  CANTIDAD POR RECETA  !  UNIDAD RECETA")

    for receta in listado:
        print("  ",receta[0],"\t\t",receta[1],"\t\t",str(receta[2])+"\t\t"+str(receta[3]),"\t\t",receta[4],) #falta comleetar el print
        input("Para continuar presione enter")

def BorrarReceta(): #funciona
    com = Modelo.Conectar()
    condicion = (input("el numro de receta a eliminar: "))
    com.DeleteReceta(condicion)

def InsertarReceta():
    con = Modelo.Conectar()

    id_receta=("\nInggrese el id de la Receta: ")
    nombre_receta =input("\nIngrese el nombre de la Receta: ")
    descrip_receta =input("\nIngrese la discripcion de la Receta: ")
    cantidad_por_receta =input("\nIngrese la cantidad por Receta: ")
    unidad_rec =input("\nIngrese la unidad de Receta: ")
    
    nuevaReceta= Modelo.Receta(id_receta,nombre_receta,descrip_receta,cantidad_por_receta,unidad_rec)

    con.InsertarProducto(nuevaReceta)
    input("Para continuar presione enter")
    


