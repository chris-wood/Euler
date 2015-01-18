# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def find_triple_with_sum(sum)
	for a in 1..(sum / 3)
		for b in a..(sum / 2)
			c = sum - b - a
			if (a**2 + b**2 == c**2)
				return [a, b, c]
			end
		end
	end
	return [1, 1, 1] # failure.
end

sumTarget = ARGV[0].to_i
triple = find_triple_with_sum(sumTarget)
product = 1
triple.each {|x| 
	product = product * x
}
puts product