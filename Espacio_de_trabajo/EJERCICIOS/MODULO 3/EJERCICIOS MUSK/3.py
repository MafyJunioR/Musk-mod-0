class Jet:

    def __init__(self, name, country, cantidad=0):
        self.name = name
        self.origin = country
        self.cantidad = cantidad

first_item = Jet("F16", "USA")
second_item = Jet('AJS37', 'Suecia')
third_item = Jet('Mirage2000', 'France', 35)
fourth_item = Jet('F14', 'USA', 87)
fifth_item = Jet('Mig29','URSS')
sixth_item = Jet('A10', 'USA')


print(first_item.name, first_item.origin, first_item.cantidad)
print(third_item.name, third_item.origin, third_item.cantidad)