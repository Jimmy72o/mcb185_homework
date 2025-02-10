t = 1, 2
print(t)
print(type(t))

def midpoint(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2) / 2
	return x, y
print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)
print(mx, my)

i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break

i = 0
while i < 3:
	i = i + 1
	print('hey', i)
	
i = 1
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)

for i in range(1, 10, 3):
	print(i)

for i in range(0, 5):
	print(i)
	
for i in range(5):
	print(i)

basket = 'milk', 'eggs', 'bread'
for thing in basket:
	print(thing)
for i in range(len(basket)):
	print(basket[i])

import random

for i in range(5):
	print(random.random())

for i in range(3):
	print(random.randint(1, 6))
