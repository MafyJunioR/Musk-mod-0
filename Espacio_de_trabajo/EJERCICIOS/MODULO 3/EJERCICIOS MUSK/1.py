class Jet:

    def __init__(self, name, country):
        self.name = name
        self.origin = country

first_item = Jet("F16", "USA")


print(first_item.name, first_item.origin)