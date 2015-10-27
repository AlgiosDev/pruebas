# -*- coding: utf-8 -*-
# See README.rst file on addon root folder for license details

def sumador():
    print "\nWhile controlado con Conteo"
    print "===========================\n"
    
    print "Un ejemplo es un sumador numérico hasta 10, \ncomo se muestra a continuación:\n"
    
    suma = 0
    numero = int(raw_input("Ingresa un numero, por favor: "))
    while numero <= 10:
        suma = numero + suma
        numero = numero + 1
    print "La suma es " + str(suma)    

#sumador()



def promedio():
    print "\nWhile controlado con Evento"
    print "===========================\n"
    
    print "Un ejemplo es calcular el promedio de grado, \ncomo se muestra a continuación:\n"
    
    promedio = 0.0
    total = 0
    contar = 0
    
    print "Introduzca valor numerico de un grado (-1 para salir): "
    grado = int(raw_input())    
    while grado != -1:
        total = total + grado
        contar = contar + 1
        print "Introduzca valor numerico de un grado (-1 para salir): "
        grado = int(raw_input())
    promedio = total / contar
    print "Promedio de grado: " + str(promedio)

#promedio()

def sentenciaBreak():
    print "\nWhile con sentencia break"
    print "=========================\n"
    
    variable = int(raw_input("Ingresa un numero, por favor: "))
    while variable > 0:
        print 'Actual valor de variable:', variable
        variable = variable -1
        if variable == 5:
            break    
    
#sentenciaBreak()   
    
def sentenciaContinue():  
    print "\nWhile con sentencia continue"
    print "============================\n"
    
    variable = int(raw_input("Ingresa un numero, por favor: "))
    while variable > 0:              
       variable = variable -1
       if variable == 5:
          continue
       print 'Actual valor de variable:', variable    

#sentenciaContinue()  
    
def fibonacci():
    a, b = 0, 1
    while b < 100:
        print b,
        a, b = b, a + b        
fibonacci()    
    
    
    
    
    
# EOF