import math
import sys

# method 1 super easy but only holds to 15 points
def nPiDigits(precision: int):
	if (precision <= 15):
		pi = round(math.pi, precision)
		print(pi)
	else:
		print("maximum printable digits is 15")

#method 2 up to 100 digits using string
def nPiDigits2(precision: int):
	pi = ("3.14159265358979323846"
			"264338327950288419716939937510582097494"
			"45923078164062862089986280348253421170679")
	if (precision <= 100):
		output = pi[0:precision + 2] # plus 2 for the 3.
		print(output)
	else:
		print("maximum printable digits is 100")

nPiDigits2(int(sys.argv[1]))
