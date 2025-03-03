class Productos:
    
    def __init__(self,nombre,precio,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def describir(self):
        return f'Nombre del producto: {self.nombre}. Precio: {self.precio}. Quedan en stock: {self.cantidad}.'
    
    def vender(self, cantidad):
        if self.cantidad > cantidad:
            self.cantidad -= cantidad
            print(f'Se vendieron {cantidad} unidades de {self.nombre}. Quedan {self.cantidad} {self.nombre}.')
        else:
            print(f'No hay suficiente stock.')
        
class Telefono(Productos):
    
    def __init__(self, nombre, precio, cantidad, marca, sistema_operativo):
        super().__init__(nombre, precio, cantidad)
        self.marca = marca
        self.sistema_operativo = sistema_operativo
        
    def describir(self):
        return f'Telefono: {self.nombre, self.marca}.Sistema Operativo: {self.sistema_operativo}. Precio: {self.precio}. Quedan en stock: {self.cantidad}.'

class PC(Productos):
    
    def __init__(self, nombre, precio, cantidad, procesador, ram):
        super().__init__(nombre, precio, cantidad)
        self.procesador = procesador
        self.ram = ram
        
    def describir(self):
        return f'Nombre del producto: {self.nombre}. Precio: {self.precio}. Quedan en stock: {self.cantidad}. \n Procesador: {self.procesador}. RAM: {self.ram}.'
    
class Accesorio(Productos):
    
    def __init__(self, nombre, precio, cantidad, tipo):
        super().__init__(nombre, precio, cantidad)
        self.tipo = tipo
        
    def describir(self):
        return f'Nombre del producto: {self.nombre}. Tipo:{self.tipo}. Precio: {self.precio}. Quedan en stock: {self.cantidad}.'
    
    
class Tienda:
    
    def __init__(self):
        self.productos = []
        
    def agregar_producto(self, producto):
        self.productos.append(producto)
        
    def mostrar_inventario(self):
        for producto in self.productos:
            print(producto.describir())
            
    def vender_producto(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto.vender(cantidad)
                return
            else:
                print(f'No se encontró el producto en el inventario.')
                
telefono1 = Telefono("iPhone 12", 999.99, 10, "Apple", "iOS")
pc1 = PC("MacBook Pro", 2500.00, 5, "Intel Core i7", 16)
accesorio1 = Accesorio("Cargador USB-C", 29.99, 50, "Cargador")


tienda = Tienda()
tienda.agregar_producto(telefono1)
tienda.agregar_producto(pc1)
tienda.agregar_producto(accesorio1)


tienda.mostrar_inventario()


tienda.vender_producto("iPhone 12", 3)
tienda.vender_producto("Cargador USB-C", 20)


tienda.mostrar_inventario()