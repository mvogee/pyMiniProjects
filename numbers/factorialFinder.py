from sys import argv

class factorial:

# this only takes O(1) space and O(n) time
	def factLoop(n: int):
		fact = n
		while (n > 1):
			n -= 1
			fact *= n
		return fact

# this takes O(n) space complexity as well as O(n) time
# in this case there is really no advantage to using recursion over the itterative solution
	def factRec(n: int):
		if (n <= 1):
			return n
		return (n * factorial.factRec(n - 1))



print(factorial.factLoop(int(argv[1])))
