class Pedido:
    def __init__(self, numero_mesa):
        self.numero_mesa = numero_mesa
        self.platos = []
        self.estado = 'Pendiente'
        
    def agregar_plato(self, plato):
        self.platos.append(plato)
        return f'Pedido de la mesa {self.numero_mesa}:\n {plato}'
    
    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ['pendiente', 'preparando', 'listo para servir']:
            self.estado = nuevo_estado
            return f'El estado del pedido de la mesa {self.numero_mesa} está {self.estado}.'
        else:
            return f'No existe dicho estado. Elige:\npendiente\npreparando\nlisto para servir.'
    
    def describir(self):
        platos_str = ", ".join(self.platos) if self.platos else "No hay platos aún"
        return f"Mesa {self.numero_mesa}, Platos: {platos_str}, Estado: {self.estado}"
    
    
pedido1 = Pedido(1)
pedido2 = Pedido(2)


print(pedido1.agregar_plato("Hamburguesa"))
print(pedido1.agregar_plato("Papas fritas"))
print(pedido2.agregar_plato("Ensalada César"))
print(pedido2.agregar_plato("Sopa de tomate"))


print(pedido1.describir())
print(pedido2.describir())


print(pedido1.cambiar_estado("en preparación"))
print(pedido1.describir())

print(pedido2.cambiar_estado("listo para servir"))
print(pedido2.describir())