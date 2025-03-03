class Animal:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
        
    def describir(self):
        return f'Nombre: {self.nombre}. Edad: {self.edad}.'
    
    def hacer_sonido(self):
        return f'El animal hace un sonido.'
    
    
class Mamifero(Animal):
    def __init__(self, nombre, edad, habitat):
        super().__init__(nombre, edad)
        self.habitat = habitat
        
    def describir(self):
        return f'Nombre: {self.nombre}. Edad: {self.edad}. Habitat: {self.habitat}.'
        
    def hacer_sonido(self):
        return 'El mamifero ruge.'
    
class Ave(Animal):
    
    def __init__(self, nombre, edad, vuela):
        super().__init__(nombre, edad)
        self.vuela = vuela
    
    def describir(self):
        return f'Nombre: {self.nombre}. Edad: {self.edad}. Vuela?: {self.vuela}.'
    
    def hacer_sonido(self):
        return 'El ave canta.'
    
class Reptil(Animal):
    
    def __init__(self, nombre, edad, venenoso):
        super().__init__(nombre, edad)
        self.venenoso = venenoso
        
    def describir(self):
        return f'Nombre: {self.nombre}. Edad: {self.edad}. Venenoso?: {self.venenoso}.'
    
    def hacer_sonido(self):
        return 'El reptil sisSsSsSsSea.'
    
class Zoologico:
    
    def __init__(self):
        self.animales = []
        
    def agregar_animal(self,animal):
        self.animales.append(animal)
        
    def mostrar_animales(self):
        for animal in self.animales:
            print(animal.describir())
            
    def hacer_sonido_todos(self):
        for animal in self.animales:
            print(animal.hacer_sonido())
    
    
mamifero1 = Mamifero('Tigre', 5, 'Bosque Tropical')
ave1 = Ave('Águila', 3, True)
reptil1 = Reptil('Cobra', 1, True)
mamifero2 = Mamifero('Elefante', 10, 'Selva')


zoo = Zoologico()
zoo.agregar_animal(mamifero1)
zoo.agregar_animal(ave1)
zoo.agregar_animal(reptil1)
zoo.agregar_animal(mamifero2)

zoo.mostrar_animales()

zoo.hacer_sonido_todos()



