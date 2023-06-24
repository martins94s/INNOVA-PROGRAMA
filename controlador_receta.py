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

def Insertar_Receta(): #funciona
    com = Modelo.Conectar()
    iD_receta = int(input("Ingrese el ID de la receta: "))
    nombre_receta = str(input("Ingrese nombre de la receta: "))
    descrip_receta = str(input("Ingrese detalle de la receta: "))
    cantidad_por_receta = int(input("Ingrese cantidad producida por la receta: "))
    unidad_rec = str(input("Ingrese la unidad de  cantidad de la receta: "))

    receta = Modelo.Receta(iD_receta,nombre_receta,descrip_receta,cantidad_por_receta,unidad_rec)

    com.InsertarReceta(receta)

def Actualizar_Receta(): #funciona
    Con = Modelo.Conectar()
    Con.UpdateReceta()

    


    

#ListarReceta() -  funciona

#BorrarReceta() - funciona

#Insertar_Receta() - funciona

#Actualizar_Receta() - funciona