import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

match = 0
for i in range(trials):
	a = 0
	birthdays = []
	for i in range(people):
		birthdays.append(random.randint(1, days))
	for i in range(0, len(birthdays)):
		for j in range(i + 1, len(birthdays)):
			if a != 0:
				break
			if birthdays[i] == birthdays[j]:
				a += 1
				match += 1
				break

print('p =', match / trials)