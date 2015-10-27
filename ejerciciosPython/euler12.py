# -*- coding: utf-8 -*-
# See README.rst file on addon root folder for license details

def euler1():
    result = 0
    for i in range(1,1000):
        if i % 3 == 0 or i % 5 == 0 :
            result = result + i
    print result



# EOF

