# 10demo.py by Jimmy Cai

print ('hello, again') # greeting

import math

print (1.5e-2)

print(1+1)

print(1-1)

print(2*2)

print(1/2)

print(2**3)

print(5//2)

print(5%2)

print(5*(2+1))

print(abs(5))

print(abs(-5))

print(pow(5,3))

print(round(1/7,ndigits=3))

print(math.ceil(5/2))

print(math.floor(5/2))

print(math.log(10))

print(math.log2(10))

print(math.log10(10))

print(math.sqrt(4))

print(math.pow(2,3))

print(math.factorial(5))

print(0.1*3)

a=3
b=4
c=math.sqrt(a**2+b**2)
print(c)
print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=', ', end='!\n')

def pythagoras(a,b):
	c=math.sqrt(a**2+b**2)
	return c
hyp=pythagoras(3,4)
print(hyp)

def circle_area(r):
	return math.pi*r**2
print (circle_area(5))

a=2
b=3
if a==b:
	print('a equals b')
print(a,b)

def is_even(x):
	if x%2 == 0: return True
	return False

print(is_even(2))
print(is_even(3))

c = a == b
print(c)
print(type(c))

if a<b: print('a < b')
elif a>b: print ('a > b')
else: print ('a == b')

if a>b or a<b: print('all things being equal, a and b are not')
if a>b and a<b: print('you are living in a strange world')
if not False: print('True')

a=.3
b=.1*3
if a<b: print('a < b')
if a>b: print('a > b')
else: print('a == b')

print(abs(a-b))
if abs(a-b) < 1e-9: print('close enough')
if math.isclose(a,b): print('close enough')

s1='A'
s2='B'
s3='a'
if s1<s2: print('A is < B')
if s2<s3: print('B is < a')

