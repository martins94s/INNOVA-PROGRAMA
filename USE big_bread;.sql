USE big_bread; 
SELECT * FROM producto;
SELECT * FROM receta;
INSERT INTO producto (iD_Producto,nombre_Producto,stock,precio,unidad_de_medida,iD_Receta) VALUES (1,"factura",5,10,"docena",1);
INSERT INTO producto (iD_Producto,nombre_Producto,stock,precio,unidad_de_medida,iD_Receta) VALUES (2,"viena",6,15,"docena",5);
INSERT INTO producto (iD_Producto,nombre_Producto,stock,precio,unidad_de_medida,iD_Receta) VALUES (4,"cañonsito",5,20,"kg",6);
INSERT INTO producto (iD_Producto,nombre_Producto,stock,precio,unidad_de_medida,iD_Receta) VALUES (5,"ojos de buey",12,18,"kg",7);
SELECT * FROM producto;
INSERT INTO receta (iD_receta,nombre_receta,descrip_receta,cantidad_por_receta,unidad_rec,) VALUES (3,"factura","harina 300g 100 azucar, 10 g levadura dulce a eleccion",5,"docena");
SELECT * FROM receta;
INSERT INTO receta (iD_receta,nombre_receta,descrip_receta,cantidad_por_receta,unidad_rec) VALUES (3,"factura","harina 300g 100 azucar, 10 g levadura dulce a eleccion",5,"docena");
INSERT INTO receta (iD_receta,nombre_receta,descrip_receta,cantidad_por_receta,unidad_rec) VALUES (4,"mignon","harina 400g 10 g sal, 10 g levadura dulce a eleccion",3,"kg");

SELECT * FROM producto;
SELECT * FROM insumo;
DELETE FROM insumo WHERE iD_insumo = "0";

TRUNCATE TABLE insumo;
SELECT * FROM insumo;
INSERT INTO insumo (iD_insumo,nombre,cantidad,insumo_unidad) VALUES (1,"harina",1000,"kg");
SELECT * FROM insumo;
INSERT INTO insumo (iD_insumo,nombre,cantidad,insumo_unidad) VALUES (2,"grasa",300,"kg");
INSERT INTO insumo (iD_insumo,nombre,cantidad,insumo_unidad) VALUES (3,"levadura",10,"kg");
INSERT INTO insumo (iD_insumo,nombre,cantidad,insumo_unidad) VALUES (4,"azucar",500,"kg");
SELECT * FROM producto;
SELECT * FROM receta;
SELECT * FROM insumo;
SELECT * FROM produccion;
INSERT INTO produccion (iD_produccion,fecha,num_pedido,prod_pedido,cantidad_pedida,unidad) VALUES (2,"01/06/2023",00002,"medialunas",30,"docena");