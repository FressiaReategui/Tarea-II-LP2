#importando las clases
from logical.forma import Forma
from logical.color import Color
#definiendo la clase y hereando de la clase
class CuadradoColor(Forma, Color):
    def __init__(self, color):
        super()
        self.color = color
        pass
