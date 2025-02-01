def char_to_prob(x):
	return 10 ** (-(ord(x) - 33) / 10)
print(char_to_prob('A'))

import math
def prob_to_char(x):
	return chr(int(-math.log10(x) * 10) + 33)
print(prob_to_char(0.001))