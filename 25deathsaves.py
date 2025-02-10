import random

a = 0
b = 0
c = 0
d = 0
while a < 10000:
	i = 0
	j = 0
	a += 1
	b = b
	c = c
	d = d
	while True:
		n = random.randint(1, 20)
		if n == 20:
			print('revived')
			b += 1
			break
		if n == 1:
			i += 2
		if n in range (2, 10):
			i += 1
		if i >= 3:
			print('die')
			c += 1
			break
		if n in range (10, 20):
			j += 1
		if j == 3:
			print('stable')
			d += 1
			break
print('p(revived) =', b / a)
print('p(die) =', c / a)
print('p(stable) =', d / a)