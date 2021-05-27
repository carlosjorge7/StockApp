create database inventario;
create table producto(
id int(11) PRIMARY KEY AUTO_INCREMENT,
nombre varchar(25),
    descripcion varchar(25),
    precio int(11),
    stock int(11)
)