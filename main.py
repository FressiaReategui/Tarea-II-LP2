#importamos las clases de los directorios
from models.gato import Gato
from models.perro import Perro

#creamos una instancia de la clase Gato
gato = Gato()
#creamos una instancia de la clase Perro
perro = Perro()

#llamamos a los metodos de la clase
gato.hacer_sonido()
perro.hacer_sonido()