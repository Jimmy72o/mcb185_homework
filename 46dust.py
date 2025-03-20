import math
import sys
import mcb185

w = int(sys.argv[2])

def entropy(seq):
	h = 0
	a = seq.count('A')
	c = seq.count('C')
	g = seq.count('G')
	t = seq.count('T')
	total = a + c + g + t
	p = [a / total, c / total, g / total, t / total]
	for val in p:
		if val != 0:
			h += (-val) * math.log2(val)
	return h

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	seq = list(seq[:1000])
	dusted = list(seq)
	for i in range(len(seq) - w + 1):
		dna = seq[i:i+w]
		if entropy(dna) < float(sys.argv[3]):
			for j in range(i, i + w):
				dusted[j] = 'N'
	print('>', defline, sep = '')
	seq = ''.join(dusted)

	for i in range(0, len(seq), 60):
		print(seq[i:i+60])