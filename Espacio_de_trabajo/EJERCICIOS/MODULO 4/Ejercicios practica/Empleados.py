class Empleado:
    def __init__(self, nombre, edad, salario_base):
        self.nombre = nombre
        self.edad = edad
        self.salario_base = salario_base

    def describir(self):
        return f"Empleado: {self.nombre}, Edad: {self.edad}, Salario Base: €{self.salario_base}"

    def calcular_salario(self):
        return self.salario_base


class Gerente(Empleado):
    def __init__(self, nombre, edad, salario_base, bono):
        super().__init__(nombre, edad, salario_base)
        self.bono = bono

    def describir(self):
        return f"Gerente: {self.nombre}, Edad: {self.edad}, Salario Base: €{self.salario_base}, Bono: €{self.bono}"

    def calcular_salario(self):
        return self.salario_base + self.bono


class Desarrollador(Empleado):
    def __init__(self, nombre, edad, salario_base, lenguaje):
        super().__init__(nombre, edad, salario_base)
        self.lenguaje = lenguaje

    def describir(self):
        return f"Desarrollador: {self.nombre}, Edad: {self.edad}, Salario Base: €{self.salario_base}, Lenguaje: {self.lenguaje}"

    def calcular_salario(self):
        if self.lenguaje.lower() == "python":
            return self.salario_base * 1.10
        else:
            return self.salario_base


class Empresa:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        for empleado in self.empleados:
            print(empleado.describir())

    def calcular_nomina_total(self):
        total = sum(empleado.calcular_salario() for empleado in self.empleados)
        return total


empleado1 = Empleado("Iker", 28, 3000)
gerente1 = Gerente("Ruben", 40, 5000, 1500)
desarrollador1 = Desarrollador("Roberto", 32, 4000, "Python")
desarrollador2 = Desarrollador("Marta", 30, 4000, "Java")

empresa = Empresa()
empresa.agregar_empleado(empleado1)
empresa.agregar_empleado(gerente1)
empresa.agregar_empleado(desarrollador1)
empresa.agregar_empleado(desarrollador2)


empresa.mostrar_empleados()


print(f"Nómina Total: €{empresa.calcular_nomina_total()}")