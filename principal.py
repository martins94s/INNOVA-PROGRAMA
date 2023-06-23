import Controlador_prod
import Controlador_insumo
import Controlador_Produccion
import Controlador_receta



while True:

    print("")
    
    print("")
    print("***********************************************************")
    print("******* Bienvenidos a la Base de Datos de Big Bread *******")
    print("***********************************************************")
    print("")
    print("MENU PRINCIPAL")
    print("")
    print("Seleccione una opcion: ")
    print("1 - INGRESAR / ELIMINAR / MODIFICACION DE PRODUCTO")
    print("2 - ALTA / BAJA / MODIFICACION DE INSUMOS")
    print("3 - ALTA / BAJA / MODIFICACION DE PRODUCCION DIARIA")
    print("4 - ALTA / BAJA / MODIFICACION DE RECETAS")
    print("5 - LISTADO DE PRODUCTOS")
    print("6 - LISTADO DE PRODUCCION EN UN INTERVALO")
    print("7 - LISTADO DE INSUMOS DIARIO")
    print("8 - SALIR")
    opcion =int(input("Ingrese su opcion: "))
    if opcion == 1: # PRODUCTO
        print("")
        print("Las Opciones de Producto son: ")
        print("")
        print("1 - Ingresar Producto")
        print("2 - Eliminar Producto")
        print("3 - Modificar Producto")
        opcion_Producto = int(input("Ingrese su opcion de Producto: "))
        if opcion_Producto == 1:
            Controlador_prod.Insertar_Producto() 
        elif opcion_Producto == 2:
            Controlador_prod.BorrarProducto()
        elif opcion_Producto == 3:
            Controlador_prod.ActualizarProducto()
        else:
            print("gracias por la consulta")


    elif opcion == 2: # INSUMO
        print("")
        print("Las Opciones de Insumos son: ")
        print("")
        print("1 - Ingresar Insumo")
        print("2 - Eliminar Insumo")
        print("3 - Modificar Insumo")
        opcion_Insumo = int(input("Ingrese su opcion de Insumo: "))
        if opcion_Insumo == 1:
            Controlador_insumo.Insertar_Insumo()
        elif opcion_Insumo == 2:
            Controlador_insumo.Borrar_Insumo()
        elif opcion_Insumo == 3:
            Controlador_insumo.Actualizar_Insumo()
        else:
            print("gracias por la consulta")

    elif opcion == 3: # PRODUCCION
        print("")
        print("Las Opciones de Produccion son: ")
        print("")
        print("1 - Ingresar Produccion")
        print("2 - Eliminar Produccion")
        print("3 - Modificar Produccion")
        opcion_Insumo = int(input("Ingrese su opcion de Produccion: "))
        if opcion_Insumo == 1:
            Controlador_Produccion.Insertar_Produccion()
        elif opcion_Insumo == 2:
            Controlador_Produccion.Borrar_Produccion()
        elif opcion_Insumo == 3:
            Controlador_Produccion.Actualizar_Produccion()
        else:
            print("gracias por la consulta")

    elif opcion == 4: # RECETA
        print("")
        print("Las Opciones de Receta son: ")
        print("")
        print("1 - Ingresar Receta")
        print("2 - Eliminar Receta")
        print("3 - Modificar Receta")
        opcion_Insumo = int(input("Ingrese su opcion de Receta: "))
        if opcion_Insumo == 1:
            Controlador_receta.Insertar_Receta()
        elif opcion_Insumo == 2:
            Controlador_receta.BorrarReceta()
        elif opcion_Insumo == 3:
            Controlador_receta.Actualizar_Receta()
        else:
            print("gracias por la consulta")

    elif opcion == 5:
        Controlador_prod.ListarProductos() #funciona

    elif opcion == 6:
        Controlador_Produccion.Listar_Produccion()

    elif opcion == 7:
        Controlador_insumo.Listar_Insumo()

    elif opcion == 8:
            break
    else:
        print("Opcion Incorrecta!!!")