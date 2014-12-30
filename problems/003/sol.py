# Problem 3. The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143?

import sys
import math

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
