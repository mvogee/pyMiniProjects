from sys import argv

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

print(primtFactorsList(int(argv[1])))
