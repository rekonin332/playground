# -*- encoding: utf-8 -*-
import sys

""" a test module """
__author__ = 'Todd Xie'


def test():


	args = sys.argv

	if len(args)==1:
		print('hello world!')
	elif len(args)==2:
		print('Hello, %s' %args[1])
	else:
		print('Too many arguments!')

def _private_1(name):
	return 'Hello, %s' %name
	
def _private_2(name):
	return 'Hi, %s' %name
	
def greeting(name):
    if len(name) > 3:
       print(_private_1(name))
    else:
        print(_private_2(name))
		
if __name__ == '__main__':
	test()
	print('hahahahaha')