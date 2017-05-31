import sys

# generate fibonacci numbers up to user defined number and return list

class fibonacci:

#return a list
	def fibList(x: int):
		if (x < 1):
			return [0]
		ret = [0, 1, 1]
		i = ret[-1]
		j = ret[-2]
		while (i + j < x):
			ret.append(i + j)
			i = ret[-1]
			j = ret[-2]
		return ret

#only print the given
	def fibPrint(x: int):
		i = 1
		j = 0
		print(j, end='')
		while (i <= x):
			print (',', i, end='')
			i = i + j
			j = i - j
		print()
		return

print(fibonacci.fibList(int(sys.argv[1])))
fibonacci.fibPrint(int(sys.argv[1]))
