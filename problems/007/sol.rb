# What is the 10001st prime number?

require 'Prime'

def lib_is_prime(n)
	return Prime.prime?(n)
end

# note that we could write special cases for small primes... but that's silly
# fact: All primes greater than 3 can be written in the form (6k +- 1).
def is_prime(n) 
	if (n % 2 == 0) # evens >2 are not prime
		return false
	elsif (n == 3)
		return true 
	else # use the 6k+-1 fact
		k = 5
		limit = Math.sqrt(n).floor() # don't bother checking past the square root

		while k <= limit
			if (n % k == 0) # 6k - 1 | n -> then n has a divisor
				return false 
			elsif (n % (k + 2) == 0) # 6k + 1 | n -> then n has a divisor
				return false
			end
			k = k + 6 
		end

		return true 
	end
end

def find_ith_prime(i)
	primes = [2]
	count = 1

	n = 3 
	while count < i # naive solution
		if lib_is_prime(n)
			if is_prime(n) 
				primes << n
				count = count + 1
			else
				puts "Error on: " + n.to_s
				return -1 # bug in my code!
			end
		end
		n = n + 2 # skip even numbers
	end

	return primes[-1]
end

prime = find_ith_prime(ARGV[0].to_i)
puts prime
