from sys import argv

def fizBuzz(size: int):
	for i in range (1, size):
		if (i % 15 == 0):
			print("fizBuzz ", i)
		elif (i % 3 == 0):
			print("fizz ", i)
		elif (i % 5 == 0):
			print("buzz ", i)

if len(argv) > 1:
	fizBuzz(int(argv[1]) + 1)
