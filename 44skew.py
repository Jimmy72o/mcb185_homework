import sys
import sequence
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	w = int(sys.argv[2])
	s = seq[:w]
	comp = sequence.gc_comp(s)
	c = s.count('C')
	g = s.count('G')
	def gc_skew(seq):
		if c + g == 0: return 0
		return (g - c) / (g + c)
	print('0', comp, gc_skew(s))
	for i in range(1, len(seq) - w + 1):
		if seq[i - 1] == 'C':
			comp -= 1 / w
			c -= 1
		if seq[i - 1] == 'G':
			comp -= 1 / w
			g -= 1
		if seq[i + w - 1] == 'C':
			comp += 1 / w
			c += 1
		if seq[i + w - 1] == 'G':
			comp += 1 / w
			g += 1
		print(i, comp, gc_skew(i))