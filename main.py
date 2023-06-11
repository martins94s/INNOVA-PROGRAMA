from conexion_bd_2 import Conectar

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
    print("9 - Insertar productos")
    print("10 - Ver productos")

    opcion = str(input("Ingrese numero: "))

    if opcion == "1":
        tor.traer_db()

    elif opcion == "2":
        tor.crear_db()

    elif opcion == "3":
        tor.eliminar_db()

    elif opcion == "4":
        tor.ver_tb_db()

    elif opcion == "5":
        tor.crear_tb_db()

    elif opcion == "6":
        tor.eliminar_tb_db()

    elif opcion == "7": 
        iD_insumo = input("Ingrese ID del insumo:")
        nombre = input("Ingrese el nombre del insumo:")
        cantidad = input("Ingrese la cantidad del insumo:")
        insumo_unidad = input("Ingrese la unidad del insumo:")
        tor.insertar_insumo_tb(iD_insumo,nombre,cantidad,insumo_unidad)

    elif opcion == "8":
        print(tor.ver_insumos_tb())

    elif opcion == "9":
        iD_Producto = input("Ingrese ID del producto:")
        nombre_Producto = input("Ingrese el nombre del producto:")
        stock = input("Ingrese stock del producto:")
        precio = input("Ingrese el precio del producto:")
        unidad_de_medida = input("Ingrese la unidad de medida del producto:")
        iD_Receta = input("Ingrese el nombre de la receta de producto:")

        tor.insertar_producto_tb(iD_Producto,nombre_Producto,stock,precio,unidad_de_medida,iD_Receta)
        
    elif opcion == "10":
        print(tor.ver_producto_tb())

    else:
        print("fin de menu") 