from sys import argv

def fizBuzz(size: int):
	for i in range (1, size):
		if (i % 15 == 0):
			print("FizzBuzz ", i)
		elif (i % 3 == 0):
			print("Fizz ", i)
		elif (i % 5 == 0):
			print("Buzz ", i)

if len(argv) > 1:
	fizBuzz(int(argv[1]) + 1)
