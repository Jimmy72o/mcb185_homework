import random

i = 0
j = 0
while True:
	n = random.randint(1, 20)
	if n == 20:
		print('revived')
		break
	if n == 1:
		i += 2
	if n in range (2, 10):
		i += 1
	if i >= 3:
		print('die')
		break
	if n in range (10, 20):
		j += 1
	if j == 3:
		print('stable')
		break