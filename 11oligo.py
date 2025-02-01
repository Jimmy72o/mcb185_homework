def tm(A, C, G, T):
	length = A + C + G + T
	if length <= 13: return (A + T) * 2 + (G + C) * 4
	else: return 64.9 + 41 * (G + C - 16.4) / length
print(tm(5, 7, 3, 4))
print(tm(1, 2, 3, 4))
print(tm(1, 3, 7, 2))
