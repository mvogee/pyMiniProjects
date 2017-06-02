import sys

# this is a comment in python
# division always returns floating point in python
# use // for floor division which discards the floating points
# use ** to for getting the power of a number 2 ** 5 is 2 to the power 5
# r before quotes in printing for raw input
# output can span multiple lines using tripple quotes """..."""
# can get sub strings by using string[start:end] start is inclusive end is excusive
# can also use slicing on arrays
# use .append mothod to append items to arrays
# we have lists aka array. list = [item, item1, item2]

def fizBuzz(size: int):
	for i in range (1, size):
		if (i != 0 and i % 15 == 0):
			print("fizBuzz ", i)
		elif (i != 0 and i % 3 == 0):
			print("fizz ", i)
		elif (i != 0 and i % 5 == 0):
			print("buzz ", i)
	return

fizBuzz(int(sys.argv[1]) + 1)
