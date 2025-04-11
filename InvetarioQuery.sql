Create Table Categoria(
    id integer primary key autoincrement,
    nombre text not null
);

Create Table Producto(
    id integer primary key autoincrement,
    nombre text not null,
    precio integer not null,
    cantidad integer not null,
    categoria_id integer not null,
    foreign key (categoria_id) references Categoria(id)
)

insert into Categoria (nombre) values ('Lacteos');
insert into Categoria (nombre) values ('Carnes');
insert into Categoria (nombre) values ('Verduras');
insert into Categoria (nombre) values ('Frutas');
insert into Categoria (nombre) values ('Granos');
insert into Categoria (nombre) values ('Otros');
insert into Producto (nombre, precio, cantidad, categoria_id) values ('Leche', 20, 10, 1);
insert into Producto (nombre, precio, cantidad, categoria_id) values ('Yogur', 15, 20, 1);
insert into Producto (nombre, precio, cantidad, categoria_id) values ('Carne de res', 100, 5, 2);
insert into Producto (nombre, precio, cantidad, categoria_id) values ('Carne de pollo', 50, 10, 2);
insert into Producto (nombre, precio, cantidad, categoria_id) values ('Zanahoria', 5, 30, 3);
insert into Producto (nombre, precio, cantidad, categoria_id) values ('Lechuga', 3, 20, 3);
insert into Producto (nombre, precio, cantidad, categoria_id) values ('Manzana', 10, 15, 4);
insert into Producto (nombre, precio, cantidad, categoria_id) values ('Platano', 8, 25, 4);
insert into Producto (nombre, precio, cantidad, categoria_id) values ('Arroz', 30, 50, 5);
insert into Producto (nombre, precio, cantidad, categoria_id) values ('Frijoles', 25, 40, 5);
insert into Producto (nombre, precio, cantidad, categoria_id) values ('Aceite', 50, 15, 6);
insert into Producto (nombre, precio, cantidad, categoria_id) values ('Sal', 2, 100, 6);
insert into Producto (nombre, precio, cantidad, categoria_id) values ('Pasta', 20, 30, 6);
insert into Producto (nombre, precio, cantidad, categoria_id) values ('Queso', 25, 10, 1);
insert into Producto (nombre, precio, cantidad, categoria_id) values ('Jamon', 30, 5, 2);