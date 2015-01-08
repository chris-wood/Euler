#!/usr/bin/ruby

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

require 'Prime'

class PrimeFactor
	def initialize(n, count)
		@n = n 
		@count = count
	end

	def factor
		@n
	end

	def count
		@count
	end
end

def prime_factors(n)
	factors = Prime.prime_division(n)
	factorList = []
	factors.each {|f, c|
		factorList << PrimeFactor.new(f, c)
	}
	return factorList
end

def find_minimum(x)
	factorCounts = []

	# initialize all factor counts to 0
	for i in 2..x
		factorCounts << 0
	end

	# build up the minimum required factors for even divisibility
	x.downto(2) { |i| 
		factors = prime_factors(i)
		factors.each {|f| 
			if (factorCounts[f.factor - 2] < f.count)
				factorCounts[f.factor - 2] = f.count # bump up to the minimum number of factors
			end
		}
	}

	# use the factor counts to actually compute the product
	product = 1
	for i in 2..x
		product = product * (i ** factorCounts[i - 2])
	end

	return product
end

product = find_minimum(ARGV[0].to_i)
puts product
