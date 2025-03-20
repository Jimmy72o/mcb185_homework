import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

def closest(R, G, B):
	mini = 765
	closest = ['color']
	with open(colorfile) as fp:
		for line in fp:
			words = line.split()
			colors = words[0]
			rgb = words[2].split(',')
			for i in range(len(rgb)):
				rgb[i] = int(rgb[i])
			dist = dtc([R, G, B], rgb)
			if dist < mini:
				mini = dist
				closest[0] = colors
	return closest
print(''.join(closest(R, G, B)))