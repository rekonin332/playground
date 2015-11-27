# -*- coding: utf-8 -*-
height = 1.75
weight = 60.5

bmi = weight/(height**2)
print(bmi)
if bmi < 18.5:
    print("over ligth")
elif bmi>=18.5 and bmi <=25:
	print("over weigth")
else:
	print("over weight!")