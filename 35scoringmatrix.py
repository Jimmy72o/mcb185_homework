import sys

nucleotides = list(sys.argv[1])
matching = sys.argv[2]
mismatch = sys.argv[3]

print('   ', end='')
for i in nucleotides:
	print(i, end='  ') 
print()

for i in range(len(nucleotides)):
	row = [nucleotides[i]]
	for j in range(len(nucleotides)):
		if nucleotides[i] == nucleotides[j]:
			row.append(matching)
		else:
			row.append(mismatch)		
	print(' '.join(row))