import math
import sys

def nPiDigits(precision: int):
	if (precision <= 15):
		pi = round(math.pi, precision)
		print(pi)
	else:
		print("maximum printable digits is 15")

nPiDigits(int(sys.argv[1]))
