# Problem 3. The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143?

import sys
import math

def g(x, n):
	return ((x ** 2) + 1) % n

def gcd(a, b):
	if (a == 0):
		return b
	elif (b == 0):
		return a
	elif (a > b):
		ar = a % b # a = bq + r, br = r
		return gcd(b, ar)
	else:
		br = b % a # b = aq + r, br = r
		return gcd(a, br)

# http://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
def factorByRho(n):
	x = 2
	y = 2
	d = 1
	while d == 1:
		x = g(x, n)
		y = g(g(x, n), n)
		d = gcd(abs(x - y), n)
	if (d == n):
		return []
	else:
		return [d]

def factor(n):
	factors = []
	maxFactor = math.sqrt(n) # factors cannot be larger than sqrt(n)
	divisor = 3 # smallest odd prime factor 

	# 2 is a special case since removing the factor is fast via bit shifting
	while (n % 2 == 0):
		n = n >> 1
		factors.append(2)

	# proceed to strip out the remaining factors
	while (n > 1 and divisor < maxFactor):
		if (n % divisor == 0):
			while (n % divisor == 0):
				n = n / divisor
				factors.append(divisor)
		divisor = divisor + 1

	# if we have exceeded the square root, the remaining factor must be prime
	if (divisor >= maxFactor and n != 1):
		factors.append(n)

	return factors

n = 100
if (len(sys.argv) == 2):
	n = int(sys.argv[1])

factors = factor(n)
print factors
print max(factors)
