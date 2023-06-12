class Producto():
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
        self.Unidad_de_medida=unidad_de_medida
        self.ID_Receta =iD_Receta
    
    def getiD_Producto(self):
        return self.iD_Producto
    def getnombre_Producto(self):
        return self.nombre_Producto
    def getUnidad_de_medida(self):
        return self.Unidad_de_medida
    def getprecio(self):
        return self.precio
  
    
    def setiD_Producto(self,iD_Producto):
        self.iD_Producto = iD_Producto
    def setnombre_Producto(self,nombre_Producto):
        self.nombre_Producto = nombre_Producto
    def setprecio(self,precio):
        self.precio = precio
    def setunidad_de_medida(self,unidad_de_medida):
        self.unidad_de_medida =unidad_de_medida
 
 class PRODUCCION():
     fecha = "",
     id_produccion= 0,
     id_producto = 0,
     cantidad= 0

     def __init__(self,fecha,id_producccion,id_producto,cantidad):
         self.fecha=fecha
         self.id_produccion=id_producccion
         self.id_producto=id_producto
         self.cantidad=cantidad

     def getfecha(self):
         return self.fecha
     def getid_produccion(self):
         return self.id_produccion
     def getid_producto(self):
         return self.id_producto
     def getcantidad(self):
         return self.cantidad
     
     def setfecha(self,fecha):
         self.fecha=fecha
     def setid_produccion(self,id_produccion):
         self.id_produccion=id_produccion
     def setidproducto(self,id_producto):
         self.id_producto=id_producto
     def setid_cantidad(self,cantidad):
         self.cantidad=cantidad


class RECETA():
    id_receta = 0,
    id_producto = 0,
    receta = "",
    cantidad= 0

    def __init__(self,id_receta,id_producto,receta,cantidad) -> None:
        self.id_receta=id_receta
        self.id_producto=id_producto  
        self.receta=receta
        self.cantidad=cantidad

    def getid_receta(self):
         return self.id_receta
    def getid_producto(self):
         return self.id_producto
    def getreceta(self):
         return self.receta
    def getcantidad(self):
         return self.cantidad
     
    def setid_receta(self,id_receta):
         self.id_receta=id_receta
    def setid_producto(self,id_producto):
         self.id_producto=id_producto
    def setreceta(self,receta):
         self.receta=receta
    def setcantidad(self,cantidad):
         self.cantidad=cantidad


class INSUMO():

    def __init__(self,id_insumo,nombre_Producto,Unidad_de_medida) -> None:
        self.id_isumo=id_insumo
        self.nombre_Producto=nombre_Producto
        self.Unidad_de_medida=Unidad_de_medida

     def getid_insumo(self):
         return self.id_isumo
    def getnombre_Producto(self):
         return self.nombre_Producto
    def getUnidad_de_medida(self):
         return self.Unidad_de_medida
     
    def setid_insumo(self,id_insumo):
         self.id_insumo=id_insumo
    def setnombre_Producto(self,nombre_Producto):
         self.nombre_Producto=nombre_Producto
    def setUnidad_de_medida(self,Unidad_de_medida):
         self.Unidad_de_medida=Unidad_de_medidaclass Producto():
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
        self.Unidad_de_medida=unidad_de_medida
        self.ID_Receta =iD_Receta
    
    def getiD_Producto(self):
        return self.iD_Producto
    def getnombre_Producto(self):
        return self.nombre_Producto
    def getUnidad_de_medida(self):
        return self.Unidad_de_medida
    def getprecio(self):
        return self.precio
  
    
    def setiD_Producto(self,iD_Producto):
        self.iD_Producto = iD_Producto
    def setnombre_Producto(self,nombre_Producto):
        self.nombre_Producto = nombre_Producto
    def setprecio(self,precio):
        self.precio = precio
    def setunidad_de_medida(self,unidad_de_medida):
        self.unidad_de_medida =unidad_de_medida
 
 class PRODUCCION():
     fecha = "",
     id_produccion= 0,
     id_producto = 0,
     cantidad= 0

     def __init__(self,fecha,id_producccion,id_producto,cantidad):
         self.fecha=fecha
         self.id_produccion=id_producccion
         self.id_producto=id_producto
         self.cantidad=cantidad

     def getfecha(self):
         return self.fecha
     def getid_produccion(self):
         return self.id_produccion
     def getid_producto(self):
         return self.id_producto
     def getcantidad(self):
         return self.cantidad
     
     def setfecha(self,fecha):
         self.fecha=fecha
     def setid_produccion(self,id_produccion):
         self.id_produccion=id_produccion
     def setidproducto(self,id_producto):
         self.id_producto=id_producto
     def setid_cantidad(self,cantidad):
         self.cantidad=cantidad


class RECETA():
    id_receta = 0,
    id_producto = 0,
    receta = "",
    cantidad= 0

    def __init__(self,id_receta,id_producto,receta,cantidad) -> None:
        self.id_receta=id_receta
        self.id_producto=id_producto  
        self.receta=receta
        self.cantidad=cantidad

    def getid_receta(self):
         return self.id_receta
    def getid_producto(self):
         return self.id_producto
    def getreceta(self):
         return self.receta
    def getcantidad(self):
         return self.cantidad
     
    def setid_receta(self,id_receta):
         self.id_receta=id_receta
    def setid_producto(self,id_producto):
         self.id_producto=id_producto
    def setreceta(self,receta):
         self.receta=receta
    def setcantidad(self,cantidad):
         self.cantidad=cantidad


class INSUMO():

    def __init__(self,id_insumo,nombre_Producto,Unidad_de_medida) -> None:
        self.id_isumo=id_insumo
        self.nombre_Producto=nombre_Producto
        self.Unidad_de_medida=Unidad_de_medida

     def getid_insumo(self):
         return self.id_isumo
    def getnombre_Producto(self):
         return self.nombre_Producto
    def getUnidad_de_medida(self):
         return self.Unidad_de_medida
     
    def setid_insumo(self,id_insumo):
         self.id_insumo=id_insumo
    def setnombre_Producto(self,nombre_Producto):
         self.nombre_Producto=nombre_Producto
    def setUnidad_de_medida(self,Unidad_de_medida):
         self.Unidad_de_medida=Unidad_de_medida