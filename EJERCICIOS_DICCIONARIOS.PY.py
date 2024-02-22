class Ejercicio1:
    def __init__(self, diccionario):
        self.diccionario = diccionario
        pass
    def add(self, key, value):
        self.diccionario[key] = value
        pass
    def remove(self, key):
        del self.diccionario[key]
        pass
    def update(self, key, value):
        self.diccionario[key] = value
        pass
    def print_all(self):
        print(self.diccionario)
        pass

instance=Ejercicio1({})
instance.add("key1", "value1")
instance.add("key2", "value2")
instance.remove("key1")
instance.update("key2", "value3")
instance.print_all()

class Ejercicio2:
    def __init__(self, texto):
        self.texto = texto
        self.diccionario = {}
        pass
    def split_text(self):
        #iterate over text
        for i in self.texto.split(" "):
            #evaluate if word is in dictionary
            if i in self.diccionario:
                self.diccionario[i] += 1
            else:
                self.diccionario[i] = 1
        pass
    def print_all(self):
        print(self.diccionario)
        pass

instance=Ejercicio2("Hello World Hello pedro World pedro pedro pedro")
instance.split_text()
instance.print_all()

class Ejercicio3:
    def __init__(self):
        self.diccionario = {}
        pass
    def add_student(self,dni,data):
        self.diccionario[dni] = data
        pass
    def print_all(self):
        print(self.diccionario)
        pass

instance=Ejercicio3()
instance.add_student(71102324, {"nombre": "pedro","edad": 20,"notas":[20,13,1]})
instance.add_student(20042421, {"nombre": "pedro","edad": 30,"notas":[20,3,14]})
instance.print_all()

class Ejercicio4:
    def __init__(self):
        self.diccionario = {}
        pass
    def add(self, key, value):
        self.diccionario[key] = value
        pass
    def remove(self, key):
        del self.diccionario[key]
        pass
    def update(self, key, prop, value):
        self.diccionario[key][prop] = value
        pass
    def print_all(self):
        print(self.diccionario)
        pass

instance=Ejercicio4()
instance.add("product1", {"nombre": "productname1","cantidad": 10,"precio": 20})
instance.add("product2", {"nombre": "productname2","cantidad": 10,"precio": 20})
instance.remove("product1")
instance.update("product2", "precio", 30)
instance.print_all()

class Ejercicio5:
    def __init__(self):
        self.diccionario = {}
        self.counter = 0
        pass
    def add_person(self, name,phone):
        self.counter += 1
        self.diccionario[self.counter] = {"name": name,"phone": phone}
        return self.counter
    def edit_person(self, id, prop, value):
        self.diccionario[id][prop] = value
        pass
    def remove_person(self, id):
        del self.diccionario[id]
        pass
    def get_person(self, id):
        print(self.diccionario[id])
        pass
    def print_all(self):
        print(self.diccionario)
        pass

instance=Ejercicio5()
person_id=instance.add_person("pedro", 71102324)
instance.edit_person(person_id, "phone", 51102324)
instance.get_person(person_id)
instance.remove_person(person_id)
instance.print_all()
person_id=instance.add_person("fresia", 71102324)
instance.get_person(person_id)
instance.print_all()

import uuid
class Ejercicio6:
    def __init__(self):
        self.diccionario = {}
        pass
    def add_tarea(self, name,state):
        instance_uuid=str(uuid.uuid4())
        self.diccionario[instance_uuid] = {"name": name,"state": state}
    def print_all(self):
        print(self.diccionario)

instance=Ejercicio6()
instance.add_tarea("tarea1", "pendiente")
instance.add_tarea("tarea2", "realizada")
instance.add_tarea("tarea3", "pendiente")
instance.print_all()

class Ejercicio7:
    def __init__(self):
        self.diccionario = {
            "m": {"descripcion_convertida": "cm","entre": 100},
            "cm": {"descripcion_convertida": "m","entre": 100},
        }
        pass
    def add(self, conversion,valor):
        get_conversion = self.diccionario[conversion]
        get_descripcion = get_conversion["descripcion_convertida"]
        get_multiplicador = get_conversion["entre"]
        if(get_descripcion=="m"):
            print('el valor convertido es {0} {1}'.format(valor/get_multiplicador,get_descripcion))
        else:
            print('el valor convertido es {0} {1}'.format(valor*get_multiplicador,get_descripcion))
        pass

instance=Ejercicio7()
instance.add("m", 10)
instance.add("cm", 10)

class Ejercicio8:
    def __init__(self):
        self.diccionario = {}
        pass
    def add_student(self,dni,name,curse):
        self.diccionario[dni] = {"name": name,"curse": curse}
        pass
    def edit_student(self, dni, prop, value):
        self.diccionario[dni][prop] = value
        pass
    def remove_student(self, dni):
        del self.diccionario[dni]
        pass
    def print_all(self):
        print(self.diccionario)
        pass

instance=Ejercicio8()
instance.add_student(71102324, "pedro", {
    "comunicacion": 10,
    "ingles": 10,
    "matematicas": 10
})
instance.add_student(20042421, "fresia", {
    "comunicacion": 10,
})
instance.print_all()

class Ejercicio9:
    def __init__(self):
        self.diccionario = {}
        pass
    def add_book(self,key,data):
        self.diccionario[key] = data
        pass
    def print_all(self):
        print(self.diccionario)
        pass

instance=Ejercicio9()
instance.add_book("book1", {
    "autor": "author1",
    "titulo": "title1",
    "ano": 2020
})
instance.add_book("book2", {
    "autor": "author2",
    "titulo": "title2",
    "ano": 2021
})
instance.print_all()

class Ejercicio10:
    def __init__(self):
        self.diccionario = {}
        pass
    def add_employee(self,key,data):
        self.diccionario[key] = data
        pass
    def print_all(self):
        print(self.diccionario)
        pass

instance=Ejercicio10()
instance.add_employee("Empleado1", {
    "nombre": "pedro",
    "posicion": "desarrollador",
    "salario": 100
})
instance.add_employee("Empleado2", {
    "nombre": "fresia",
    "posicion": "CEO",
    "salario": 200
})
instance.print_all()

class Ejercicio11:
    def __init__(self):
        self.diccionario = {}
        pass
    def add_habitacion(self,key, info,state):
        self.diccionario[key] = {"info": info,"state": state}
    def print_all(self):
        print(self.diccionario)

instance=Ejercicio11()
instance.add_habitacion(1,
    {
        "banos": 2,
        "habitaciones": 3
    }
, "ocupado")
instance.add_habitacion(2,
    {
        "banos": 2,
        "habitaciones": 3
    }
, "reservado")
instance.add_habitacion(3,{
    "banos": 2,
    "habitaciones": 3
},"disponible")
instance.print_all()

class Ejercicio12:
    def __init__(self):
        self.diccionario = {}
        pass
    def add_profile(self,key, info,seguidores,social):
        self.diccionario[key] = {"info": info,"seguidores": seguidores,"social":social}
    def print_all(self):
        print(self.diccionario)

instance=Ejercicio12()
instance.add_profile(1,{
    "name": "pedro",
    "age": 20,
    "city": "bogota",
    "country": "colombia"
},10000,"facebook")
instance.add_profile(2,{
    "name": "fresia",
    "age": 20,
    "city": "bogota",
    "country": "colombia"
},10000,"instagram")
instance.add_profile(3,{
    "name": "pedro",
    "age": 20,
    "city": "bogota",
    "country": "colombia"
},10000,"whatsapp")
instance.print_all()
class Ejercicio13:
    def __init__(self):
        self.diccionario = {
            "brillo": 10,
            "resolucion": 100,
            "color": "negro",
            "tamanio": "pequenio"
        }
        pass
    def add_config(self,key, info):
        self.diccionario[key] = info
        pass
    def deactive_config(self,key):
        self.diccionario[key] = None
        pass
    def print_all(self):
        print(self.diccionario)

instance=Ejercicio13()
instance.add_config("brillo", 140)
instance.add_config("resolucion", 1306)
instance.add_config("color", "rosa")
instance.add_config("tamanio", "grande")
instance.print_all()

class Ejercicio14:
    def __init__(self):
        self.diccionario = {}
        pass
    def add_activity(self,day, month,activity):
        self.diccionario[day,'-',month] = activity
        pass
    def print_all(self):
        print(self.diccionario)

instance=Ejercicio14()
instance.add_activity(1, "enero",{
    "tarea": "hacer ejercicio",
    "duracion": "2 horas"
})
instance.add_activity(2, "enero",{
    "tarea": "estudiar",
    "duracion": "2 horas"
})
instance.add_activity(10, "enero",{
    "tarea": "ir al super",
    "duracion": "1 horas"
})
instance.add_activity(14, "enero",{
    "tarea": "pasear a los perros",
    "duracion": "2 horas"
})
instance.add_activity(20, "enero",{
    "tarea": "ayudar a mi mama",
    "duracion": "2 horas"
})
instance.print_all()

class Ejercicio15:
    def __init__(self):
        self.diccionario = {}
        pass
    def add_cantidato(self,candidato,votos):
        self.diccionario[candidato] = votos
        pass
    def print_all(self):
        print(self.diccionario)
    
instance=Ejercicio15()
instance.add_cantidato("pedro", 100)
instance.add_cantidato("castle", 200)
instance.add_cantidato("pedro", 300)
instance.add_cantidato("fresia", 400)
instance.add_cantidato("maduro", 500)
instance.print_all()

class Ejercicio16:
    def __init__(self):
        self.diccionario = {}
        pass
    def add_proyecto(self,key,info,miembros):
        self.diccionario[key] = {
            "info": info,
            "miembros":miembros
        }
        pass
    def print_all(self):
        print(self.diccionario)

instance=Ejercicio16()
instance.add_proyecto(1,{
    "nombre": "proyecto 1",
    "lider": "pedro",
},["fresia","pedro"])
instance.add_proyecto(2,{
    "nombre": "proyecto 2",
    "lider": "pedro",
},["fresia","pedro"])
instance.add_proyecto(3,{
    "nombre": "proyecto 3",
    "lider": "pedro",
},["fresia","pedro"])
instance.print_all()