import math
def triples(n):
	for a in range(1, n):
		for b in range(a, n):
			c = math.sqrt(a**2 + b**2)
			if c % 1 == 0: print(a, b, c)
triples(100)