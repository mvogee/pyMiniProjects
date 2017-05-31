import sys

def primeFactors(x: int):
	for i in range (1, x // 2):
		j = x // i
		if (i*j == x):
			print(i, end='*')
			print(j, end=',')
	print()
	return

def primtFactorsList(x: int):
	lst = []
	for i in range(1, x // 2):
		j = x // i
		if (i*j == x):
			if (i not in lst):
				lst.append(i)
			if (j not in lst):
				lst.append(j)
	return lst
primeFactors(int(sys.argv[1]))
print(primtFactorsList(int(sys.argv[1])))
