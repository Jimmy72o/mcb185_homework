import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

match = 0
for i in range(trials):
	calendar = []
	for i in range(days):
		calendar.append(0)
	for i in range(people):
		birthday = random.randint(0, days - 1)
		if calendar[birthday] == 1:
			match += 1
			break
		calendar[birthday] += 1

print('p =', match / trials)