# -*- coding: utf-8 -*-
# See README.rst file on addon root folder for license details

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Coord: " + str(self.__dict__)
    
def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)

def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)

one = Coordinate(100, 200)
print one
two = Coordinate(300, 200)
print two
three = Coordinate(-100, -100)
print three

resulAdd = add(one, three)
print resulAdd

resulSub = sub(one, two)
print resulSub



def wrapper(func):
     def checker(a, b): # 1
         if a.x < 0 or a.y < 0:
             a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
         if b.x < 0 or b.y < 0:
             b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
         ret = func(a, b)
         if ret.x < 0 or ret.y < 0:
             ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
         return ret
     return checker

add = wrapper(add)
sub = wrapper(sub)
print sub(one, two)
print add(one, three)



def one(*args):
    print args
    
one()  
one(1, 2, 3)  



def two(x, y, args):
    print x, y, args
    
two('a', 'b', 'c')



def add(x, y):
    return x + y

lst = [1, 2]
print add(lst[0], lst[1])
print add(*lst)





# EOF
    