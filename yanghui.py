# -*- encoding:utf-8 -*-
def triangle():
    b = [1]
    while True:
        yield b
        b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] + [1]
		
def triangle2(x):
	if(x == 1):
	    b = [1]
	    print(b)
	else:
	    triangle2(x-1)
   
		
	b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] + [1]
	print(b)
	