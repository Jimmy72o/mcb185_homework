def fibonacci(n):
	x1 = 0
	x2 = 1
	for i in range(n-1):
		print(x1)
		x3 = x1 + x2
		x1 = x2
		x2 = x3
	return x1
print(fibonacci(10))
