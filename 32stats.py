import sys
import math

values = []
for arg in sys.argv[1:]:
	values.append(float(arg))

values.sort()

print(values)

print('number of values:', len(values))

min = values[0]
max = values[0]
for value in values[1:]:
	if value < min:
		min = value
print('minimum value:', min)
for value in values[1:]:
	if value > max:
		max = value
print('maximum value:', max)

def mean(x):
	total = 0
	for value in values:
		total += value
	return total / len(values)
print('mean:', mean(values))

def sd(x):
	total = 0
	for value in values:
		total += (value - mean(x)) ** 2
	return (total / (len(x) - 1)) ** .5
print('standard deviation:', sd(values))

if len(values) % 2 != 0:
	print('median:', values[math.floor(len(values) / 2)])
else:
	print('median:', (values[int(len(values) / 2)] + values[int(len(values) / 2) - 1]) / 2)