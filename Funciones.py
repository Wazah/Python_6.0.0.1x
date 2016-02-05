# -*- coding: cp1252 -*-
name=raw_input('ingresa un string plz ')
'a' in 'asd'
print('text')
##comment
#comment too
x=float(raw_input('un número plz(x): '))
x=x*x
print(x)
y=float(raw_input('otro número plz(y): '))
print(y*y)

if True|False:
	print('True or False = True')
else:
	print('hi')
print('fuera del if por la dentacion')

if x%2==0:
	print('x is odd')
else:
	print('x is even')
print('next')

if x%2==0:
	if x%3==0:
		print('x is Divisible by 2 and 3')
	else:
		print('x is Divisible by 2 and not by 3')
elif x%3==0:
	print('x is Divisible by 3 and not by 2')
else:
	print('x is Not divisible by 2 or 3')

#Para comparar floats usar abs(x-y)<0.0001 en vez de x==y