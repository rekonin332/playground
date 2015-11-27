# -*- encoding:utf-8 -*-
from collections import Iterable
from functools import reduce
def normalize(L):
	if not isinstance(L,list):
	    #print("please enter a list")
		return None
	def toFirstLower(y):
		if len(y) == 0:
			return
		first = str(y[0]).upper()
		return first + y[1:]
		
	L2 = list(map(lambda x:toFirstLower(x),L))
	print(L2)
	

def sum(L3):
    return reduce(lambda x, y: x+y,L3)		
	 
def prod():
	return reduce(lambda x, y: x*y, [3,5,7,9])
	 

def normalize2(seq):
    return list(map(lambda arg:(arg[0].upper()+arg[1:].lower()),seq))	