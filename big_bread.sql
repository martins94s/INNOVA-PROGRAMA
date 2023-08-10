CREATE DATABASE big_bread; 
USE big_bread;

CREATE TABLE PRODUCTO(
ID_PRODUCTO int not null PRIMARY key AUTO_INCREMENT,
nombre_Producto varchar(100), 
Stock int, 
precio int ,
Unidad_de_medida varchar (15),
id_receta int not null,
FOREIGN KEY (ID_Receta) REFERENCES Productos(ID_Producto));

 CREATE TABLE PRODUCCION(
ID_Produccion int primary key auto_increment,
Fecha int not null,
Num_Pedido int not null,
Prod_Pedido varchar (50),
Cantidad_Pedida int not null,
Unidad varchar (50));

CREATE TABLE RECETA(
id_receta int primary key auto_increment, 
nombre_receta varchar (50),
descrip_receta varchar(300),
cantidad_por_receta int,
unidad_rec varchar (30)
);  
 
CREATE TABLE INSUMOS(
id_insumo int primary key auto_increment,
nombre varchar (50) not null,
cantidad int not null,
insumo_unidad int not null);

