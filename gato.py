# llamamos la clase Animal abstracta
from logical.animal import Animal
class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")