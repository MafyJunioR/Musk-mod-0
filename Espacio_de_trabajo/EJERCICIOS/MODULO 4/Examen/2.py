from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def preprocess_data(self, data = None, y = None):
        pass
    
    @abstractmethod
    def fit(self):
        pass
    
    @abstractmethod
    def predict(self):
        pass
    
class SVM(Model):
    
    def preprocess_data(self, data = None, y = None):
        self.data = data
        self.y = y 
        print(f'Preprocessing data at {self.__class__.__name__}.')          
        
    def fit(self):
        print(f'Training at {self.__class__.__name__}.')
        
    def predict(self):
        print(f'Evaluating at {self.__class__.__name__}.')
        
class DecisionTree(SVM):
    def __init__(self) -> None:
        super().__init__()
        
# Hay que ser igual de listo que de vago. :)  ({self.__class__.__name__})
        
print('\nSVM:')
svm = SVM()
svm.preprocess_data(data=None, y=None)
svm.fit()
svm.predict()

print('\nDecisionTree:')
dt = DecisionTree()
dt.preprocess_data(data=None, y=None)
dt.fit()
dt.predict()



print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')



class SVM:
    def __init__(self) -> None:
        pass

    def preprocess_data(self, data = None, y = None):
        self.data = data
        self.y = y 
        print(f'Preprocessing data at {self.__class__.__name__}.')          
        
    def fit(self):
        print(f'Training at {self.__class__.__name__}.')
        
    def predict(self):
        print(f'Evaluating at {self.__class__.__name__}.')
        
class DecisionTree(SVM):
    def __init__(self) -> None:
        super().__init__()
        
# Hay que ser igual de listo que de vago. :)  ({self.__class__.__name__})
        
print('\nSVM:')
svm = SVM()
svm.preprocess_data()
svm.fit()
svm.predict()

print('\nDecisionTree:')
dt = DecisionTree()
dt.preprocess_data()
dt.fit()
dt.predict()

print('\n______________________________________\n')
print('\n______________________________________\n')
print('\n______________________________________\n')


from abc import ABC

class Algoritmo:
    def __init__(self, nombre, tarea, aprendizaje):
        self.nombre = nombre
        self.tarea = tarea
        self.aprendizaje = aprendizaje

class BaseClasiffier(Algoritmo):
    def __init__(self, nombre, tarea, aprendizaje):
        super().__init__(nombre, tarea, aprendizaje)
        
print(issubclass(BaseClasiffier, Algoritmo))