# -*- coding: utf-8 -*-

def numeros(): 
    numero = int(raw_input("Ingresa un entero, por favor: "))
    if numero < 0:
        numero = 0
        print 'Numero negativo cambiado a cero'
    elif numero == 0:
        print 'Numero es Cero'
    elif numero == 1:
        print 'Numero Simple'
    else:
        print 'Mayor que uno'

numeros() 


def asignaciones():
    a = int(raw_input("Ingresa un entero, a: "))
    b = int(raw_input("Ingresa un entero, b: "))
    c = int(raw_input("Ingresa un entero, c: "))

    print "el valor de la variable 'a' es:", a
    print "el valor de la variable 'b' es:", b

    c = a + b
    print "Operador + | El valor de la variable 'c' es ", c

    c += a
    print "Operador += | El valor de la variable 'c' es ", c 

    c *= a
    print "Operador *= | El valor de la variable 'c' es ", c 

    c /= a 
    print "Operador /= | El valor de la variable 'c' es ", c 

    c = 2
    c %= a
    print "Operador %= | El valor de la variable 'c' es ", c

    c **= a
    print "Operador **= | El valor de la variable 'c' es ", c

    c //= a
    print "Operador //= | El valor de la variable 'c' es ", c

asignaciones() 




def operadoresLogicos():

    a = int(raw_input("Ingresa un entero, a: "))
    b = int(raw_input("Ingresa un entero, b: "))
    
    print "el valor de la variable 'a' es:", a
    print "el valor de la variable 'b' es:", b
    
    if ( a and b ):
       print "Operador and | a y b son VERDADERO"
    else:
       print "Operador and | O bien la variable 'a' no es VERDADERO o la variable 'b' no es VERDADERO"
    
    if ( a or b ):
       print "Operador or | O bien la variable 'a' es VERDADERA o la variable 'b' es VERDADERA o ambas variables son VERDADERA"
    else:
       print "Operador or | Ni la variable 'a' es VERDADERA ni la variable 'b' es VERDADERA"
    
    if not( a and b ):
       print "Operador not | Ni la variable 'a' NO es VERDADERA o la variable 'b' NO es VERDADERA"
    else:
       print "Operador not | las variables 'a' y 'b' son VERDADERAS"    
     
operadoresLogicos() 



         