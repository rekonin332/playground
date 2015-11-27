# -*- encoding:utf-8 -*-
L = ['Bart','Lisa','Adam']
for l in L:
	print("hello, %s"%l)

i = 0;	
while True:	
	print("hello,{}".format(L[i]))
	if i<len(L)-1:
		i = i + 1
	else:
		break
		
