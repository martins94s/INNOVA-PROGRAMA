CREATE DATABASE big_BREADD;
USE big_BREADD;
CREATE TABLE PRODUCCION(
fecha date NOT NULL,
 id_produccion int primary key auto_increment,
 id_producto int not null,
 cantidad int not null);
 
CREATE TABLE PRODUCTO(
id_producto int not null,
 nombre varchar(30), 
 descripcion varchar(300),
 precio decimal(5,5)not null);
 
CREATE TABLE RECETA(
id_receta int primary key auto_increment,
id_producto int ,
receta varchar(300),
 cantidad int);
 
CREATE TABLE INSUMOS(
id_insumo int primary key auto_increment,
nombre varchar (50) not null,
descripcion varchar(300));
 
 insert into producto(producto,receta,precio)
 values
  ('factuas', 'por unidad', 120.00),
  ('criollos', '100 gramos', 100),
  ('pan', 'la tira ',50 );
  
  insert into produccion(id_producto,fecha,cantidad)
  values
(1,'6/6/023',150),
(2, '7/6/2023',150),
(3,'2023-05-22', 100);

insert into insumo(id_insumo,nombre,descripcion)
values
  ('harina', 'para hacer la masa'),
  ('levadura', 'se alimenta de los azúcares presentes en la harina o el mosto'),
  ('leche', 'Incorpora al pan más nutrientes, elevando su valor proteico'),
  ('crema pastelera', 'aporta humedad, sabor y textura a las masas dulces'),
  ('agua', 'Hidrata la harina y permite la formación y el desarrollo del gluten'),
  ('sal', ' potencia el sabor del pan, fortalece el gluten, frena la actividad de la levadura'),
  ('azucar', 'Es un alimento de la levadura, que produce CO2 y alcohol al fermentar el azúcar y hace que la masa crezca y se esponje');
  
  insert into receta (id_producto,receta,cantidad)
  values
  (1,'medialunas',100),
  (1,'facturas de crema pastelera',150),
  (2,'criollos dulces',300),
  (2,'criollos salados',400),
  (3,'pan flauta',80),
  (3,'pan miñon',70);
  