# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares(n)
	return ((n * (n + 1) * (2*n + 1)) / 6)
end

def square_of_sums(n)
	return (((n * (n + 1)) / 2) ** 2)
end

target = ARGV[0].to_i
sums = sum_of_squares(target)
squares = square_of_sums(target)
puts (sums - squares).abs