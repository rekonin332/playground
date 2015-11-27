# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    delta=b**2-4*a*c
    if (delta < 0):
        return("无解")
    elif (delta > 0):
        x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
        return(x1,x2)