# Problem 1. Find the sum of all the multiples of 3 or 5 below 1000.

import sys
upperBound = int(sys.argv[1])

def sumDivisibleByN(limit, n):
	m = limit / n 
	# sum_{i=0}^{m} = [m(m+1)] / 2
	return n * ((m * (m + 1)) / 2)

# fast way
by3 = sumDivisibleByN(upperBound - 1, 3)
by5 = sumDivisibleByN(upperBound - 1, 5)
by15 = sumDivisibleByN(upperBound - 1, 15)
print (by3 + by5 - by15)

# slow way
ssum = 0
for i in range(upperBound):
	if (i % 3 == 0) or (i % 5 == 0):
		ssum = ssum + i
print ssum
