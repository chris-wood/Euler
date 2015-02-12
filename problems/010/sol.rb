# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

def seive(limit)
	seiveArray = Array.new
	for i in 0..limit
		seiveArray << i
	end

	# 0 and 1 are not prime
	seiveArray[0] = 0
	seiveArray[1] = 0

	# Seive!
	divisor = 2
	loopLimit = Math.sqrt(limit)
	while (divisor < loopLimit)
		# first instance is prime, the second one won't be. 
		# e.g., 2 is prime, 4 is not, so start at 4 and step by divisor
		index = divisor * 2 
		(index..limit).step(divisor) do |i|
			seiveArray[i] = 0 # cancel it out
		end
		divisor = divisor + 1
		while (seiveArray[divisor] == 0)
			divisor = divisor + 1
		end
	end

	return seiveArray
end

limit = ARGV[0].to_i
seiveArray = seive(limit)
puts seiveArray.reduce(:+) # sum them together