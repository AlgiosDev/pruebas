# -*- coding: utf-8 -*-

##### ENTEROS ######
a = 3
print type(a)
#<type 'int'>


##### FLOAT ######
d = 0.1234
print type(d)
#<type 'float'>


##### BOOLEANOS ######
c = True
print type(c)
#<type 'bool'>


##### STRINGS ######
b = "hola"
print type(b)
#<type 'str'>


##### COMPLEJOS ######
complejo = 2.1 + 7.8j
print complejo
#(2.1+7.8j)
print type(complejo)
#<type 'complex'>


##### CADENAS ######
uno = "uno\n"
dos = "dos\n"
mix1 = uno + dos
mix2 = uno * 3
print mix1
#uno
#dos
print mix2
#uno
#uno
#uno


##### LISTAS ######
lista = ['pan', 'huevos', 100, 1234]
print lista
#['pan', 'huevos', 100, 1234]
print type(lista)
#<type 'list'>


##### TUPLAS ######
tupla = 12345, 54321, 'hola!'
print tupla
#(12345, 54321, 'hola!')
print type(tupla)
#<type 'tuple'>


##### DICCIONARIO ######
dict = {
    "nombres":"Leonardo Jose",
    "apellidos":"Caballero Garcia",
    "celular":"14522590",
    "fecha_nacimiento":"03121980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
    "nacionalidad":"Venezolana",
    "estado_civil":"Complicado"
    }
print dict.keys()
#['fecha_nacimiento', 'nombres', 'apellidos', 'celular', 'lugar_nacimiento', 'estado_civil', 'nacionalidad']
print dict.values()
#['03121980', 'Leonardo Jose', 'Caballero Garcia', '14522590', 'Maracaibo, Zulia, Venezuela', 'Complicado', 'Venezolana']
print dict.items()
#[('fecha_nacimiento', '03121980'), ('nombres', 'Leonardo Jose'), ('apellidos', 'Caballero Garcia'), ('celular', '14522590'), ('lugar_nacimiento', 'Maracaibo, Zulia, Venezuela'), ('estado_civil', 'Complicado'), ('nacionalidad', 'Venezolana')]
print dict["fecha_nacimiento"]
#03121980
print type(dict)
#<type 'dict'>















