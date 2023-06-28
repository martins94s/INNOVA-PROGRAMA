CREATE DATABASE big_BREADD; 
USE big_BREADD;

CREATE TABLE PRODUCTO(
id_producto int not null,
 nombre_Producto varchar(30), 
Unidad_de_medida varchar(10), 
 precio decimal(5,5)not null);

 CREATE TABLE PRODUCCION(
 fecha date NOT NULL,
 id_produccion int primary key auto_increment,
 id_producto int not null,
 cantidad int not null);
 
CREATE TABLE RECETA(
id_receta int primary key auto_increment, 
id_producto int ,
receta varchar(300),
 cantidad int);  
 
CREATE TABLE INSUMOS(
id_insumo int primary key auto_increment,
nombre_Producto varchar (50) not null,
Unidad_de_medida varchar(300));
 
