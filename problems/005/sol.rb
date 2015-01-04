#!/usr/bin/ruby

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def sieve_product(n)
	product = 1
	marked = []
	i = 1
	while i < n # 2..10
		marked.insert(i, 0)
		i = i + 1
	end

	i = 2
	while i < n
		j = i
		while j < n 
			print j.to_s + " "
			if marked[j - 1] == 0
				marked[j - 1] = i # flag as the mark
			end
			j = j + i
		end
		i = i + 1
		while marked[i - 1] != 0
			i = i + 1
		end
	end

	return product
end

product = sieve_product(ARGV[0].to_i)
puts product