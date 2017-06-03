from sys import argv

class factorial:

	def factIter(n: int):
		fact = n
		while (n > 1):
			n -= 1
			fact *= n
		return fact

	def factRec(n: int):
		if (n <= 1):
			return n
		return (n * factorial.factRec(n - 1))

print(factorial.factIter(int(argv[1])))
