class Staff:
    def __init__(self, role, depty, salary):
        self.role = role
        self.depty = depty
        self.salary = salary
        
class Profesor(Staff):
    def __init__(self, role, depty, salary, nombre, edad):
        super().__init__(role, depty, salary)
        self.nombre = nombre
        self.edad = edad
        
    
profesor1 = Profesor('Desarrollador', 'IT', 50000, 'Fane Spoitoru', 30)

print(profesor1.role)
print(profesor1.depty)
print(profesor1.salary)
print(profesor1.nombre)
print(profesor1.edad)

print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')


class Parent1:
    def __init__(self, x):
        self.x = x
        
    def display(self):
        print(f'In display method of Parent1: x={self.x}')


class Parent2:
    def __init__(self, y):
        self.y = y
        
    def display(self):
        print(f'In display method of Parent2: y={self.y}')
        
class Child(Parent1,Parent2):
    def __init__(self, x, y, z):
        Parent1.__init__(self,x)
        Parent2.__init__(self,y)
        self.z = z
        
    def display(self):
        print(f'In display method of Child: x={self.x}, y={self.y} and z={self.z}')
        
        
parent1 = Parent1(10)
parent1.display()

parent2= Parent2(20)
parent2.display()

child = Child(10, 20, 30)
child.display()



print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')




class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150.')

    def change_gear(self):
        print('Vehicle change 6 gear.')


class Car(Vehicle):
    def __init__(self, name, color, price):
        super().__init__(name, color, price)
        
    def max_speed(self):
        print('Car max speed is 490 km/h.')
        
    def change_gear(self):
        print('Car change 5 gear.')
        
        
vehicle1 = Vehicle('Bus','Red', 14500)
vehicle2 = Vehicle('Truck','Purple', 40000)

car1 = Car('Sedan','White',35400)
car2 = Car('Van', 'Blue', 22000)


print("Vehicle 1:")
vehicle1.show()
vehicle1.max_speed()
vehicle1.change_gear()

print("\nVehicle 2:")
vehicle2.show()
vehicle2.max_speed()
vehicle2.change_gear()

print("\nCar 1:")
car1.show()
car1.max_speed()
car1.change_gear()

print("\nCar 2:")
car2.show()
car2.max_speed()
car2.change_gear()