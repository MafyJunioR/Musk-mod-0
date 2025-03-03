class Libro:
    def __init__(self, titulo, autor, anno):
        self.titulo = titulo
        self.autor = autor
        self.anno = anno
        self.disponible = True
        
    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f'Has prestado el libro {self.titulo}.'
        else:
            return f'El libro {self.titulo} ya está prestado.'
            
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return f'Has devuelto el libro {self.titulo}.'
        else:
            return f'El libro {self.titulo} ya está prestado.'
                    
    def describir(self):
        if self.disponible == True:
            estado = 'Disponible'
        else:
            estado = 'Prestado'
        return f'Titulo: {self.titulo}. Autor: {self.autor}. Año: {self.anno}. Estado: {estado}.'
    
libro1 = Libro('Fray perico y su borrico', 'Juan Muñoz Martín', 1980)
libro2 = Libro('Metro 2033', 'Dmitri Glujovski', 2002)

print(libro1.describir())
print(libro2.describir())

libro1.prestar()
print(libro1.describir())

libro1.devolver()
print(libro1.describir())
