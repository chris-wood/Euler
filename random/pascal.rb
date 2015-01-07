#!/usr/bin/ruby

# Compute the (i,j)th element in Pascal's triangle

def get_pascal_element(i, j)
	if (j > i)
		return -1
	end

	if (i == 0)
		return 1
	end

	baseRow = [1, 1]
	currentRow = []
	for k in 2..i
		currentRow = [1] # outside is always 1
		for kk in 1..(k-1)
			currentRow << (baseRow[kk - 1] + baseRow[kk])
		end
		currentRow << 1 # outside is always 1
		baseRow = currentRow
	end

	return currentRow[j]
end

def factorial(n)
	fact = 1
	for i in 2..n
		fact = fact * i
	end
	return fact
end

# (i,j) = C(i,j) = i! / (j! * (i-j)!)
def get_pascal_element_direct(i, j)
	return (factorial(i) / (factorial(j) * factorial(i - j)))
end

i = ARGV[0].to_i
j = ARGV[1].to_i
puts get_pascal_element(i, j)
puts get_pascal_element_direct(i, j)