import random

n = random.randint(1, 20)
if n >= 5: print(n, 'success')
else: print(n, 'failure')

n = random.randint(1, 20)
if n >= 10: print(n, 'success')
else: print(n, 'failure')

n = random.randint(1, 20)
if n >= 15: print(n, 'success')
else: print(n, 'failure')

a = random.randint(1, 20)
b = random.randint(1, 20)
if a >= b:
	if a >= 5: print(a, 'success')
	else: print(a, 'failure')
if a < b:
	if b >= 5: print(b, 'success')
	else: print(b, 'failure')

a = random.randint(1, 20)
b = random.randint(1, 20)
if a >= b:
	if a >= 10: print(a, 'success')
	else: print(a, 'failure')
if a < b:
	if b >= 10: print(b, 'success')
	else: print(b, 'failure')

a = random.randint(1, 20)
b = random.randint(1, 20)
if a >= b:
	if a >= 15: print(a, 'success')
	else: print(a, 'failure')
if a < b:
	if b >= 15: print(b, 'success')
	else: print(b, 'failure')

a = random.randint(1, 20)
b = random.randint(1, 20)
if a <= b:
	if a >= 5: print(a, 'success')
	else: print(a, 'failure')
if a > b:
	if b >= 5: print(b, 'success')
	else: print(b, 'failure')

a = random.randint(1, 20)
b = random.randint(1, 20)
if a <= b:
	if a >= 10: print(a, 'success')
	else: print(a, 'failure')
if a > b:
	if b >= 10: print(b, 'success')
	else: print(b, 'failure')

a = random.randint(1, 20)
b = random.randint(1, 20)
if a <= b:
	if a >= 15: print(a, 'success')
	else: print(a, 'failure')
if a > b:
	if b >= 15: print(b, 'success')
	else: print(b, 'failure')