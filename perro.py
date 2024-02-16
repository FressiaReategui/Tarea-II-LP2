# llamamos la clase Animal abstracta
from logical.animal import Animal
class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")