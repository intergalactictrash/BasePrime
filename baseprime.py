#!/usr/bin/python
from __future__ import division
import time
import math


prime = 5
divs = [3]
primes = [3,5]

ticks = time.time()

#Finds noncomposite numbers up to prime < int
while prime < 999:
	prime +=2
	divs.append(prime-2)
	for i in divs:
		a = prime % i
		#print prime, " mod ", i, " equals ", a
		if prime % i == 0:
			break
	else:
		#print prime, " is prime"
		primes.append(prime)
print primes
ticksf = time.time()

time=ticksf-ticks
print "It took ", time, "seconds to calculate this list of primes"
"""
numbers = raw_input("enter an number: ")
print "number you chose is: ", numbers
number=int(numbers)
print type(number)

numlist = list(map(int, numbers))
print numlist
print type(numlist)
"""


"""
This function expresses integer, n in base, b.
"""

def carry(n,b):
	baselist = []
	basenumber = []
	exp = math.log(n, b) + 0.0000001
	#print exp 
	#print math.ceil(exp)
	digits = math.ceil(exp)
	#print "number of digits:", digits
	for i in range(0,int(digits)):
		baselist.append(0)
	#print baselist

	div=n//b
	basenumber.append(n%b)
	while len(basenumber) != len(baselist):
		left = div%b
		basenumber.insert(0, left)
		div=div//b
	stringnum = ''.join(str(x) for x in basenumber)
	#print stringnum
	return stringnum
	return exp
	return digits
	pass


for i in primes:

	print i, "in base 2:",carry(i,2)
	print i, "in base 3:",carry(i,3)
	print i, "in base 4:",carry(i,4)
	print i, "in base 5:",carry(i,5)
	print i, "in base 6:",carry(i,6)
	print i, "in base 7:",carry(i,7)
	print i, "in base 8:",carry(i,8)
	print i, "in base 9:",carry(i,9)
	print " "





