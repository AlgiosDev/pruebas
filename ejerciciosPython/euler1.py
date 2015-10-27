# -*- coding: utf-8 -*-

import euler12

def euler1():
    result = 0
    for i in range(1,1000):
        if i % 3 == 0 or i % 5 == 0 :
            result = result + i
    print "El resultado es %s\n" % result
euler1()





def hola():
    print "hola, mundo"
    print "¿Estás ahí?"
hola()



#invocar funciones que están dentro de otros módulos

euler12.euler1()
