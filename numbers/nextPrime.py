from math import sqrt;
from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def find_next_prime(current: int):
	prime = False
	while (prime == False):
		current += 1
		prime = isPrime(current)
	return current


def nextPrime():
	get_next = True
	prime = 2
	yes = {'y', 'yes', 'continue', 'next'}
	no = {'n', 'no', 'exit', 'quit', 'stop'}
	print(prime)
	while (get_next):
		userin = input("show next prime? y/n: ")
		if (userin.lower() in yes):
			prime = find_next_prime(prime)
			print(prime)
		elif (userin.lower() in no):
			get_next = False
		else:
			print ("invalid input")

nextPrime()
