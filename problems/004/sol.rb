#!/usr/bin/ruby

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

numDigits = 3
if ARGV.size() > 0
	numDigits = ARGV[0].to_i
end 

# check if the interet is a palindrome by converting it to a string and walking
def is_palindrome(n)
	str = n.to_s
	i = 0
	j = str.length() - 1
	while (i < j)
		if str[i] != str[j]
			return false
		end
		i = i + 1
		j = j - 1
	end
	return true
end

def find_largest_palindrome_exhaustive(low, high)
	palindromes = []
	for i in high.downto(low)
		for j in high.downto(low)
			product = i * j
			if is_palindrome(product)
				palindromes.insert(0, product)
			end
		end
	end 
	return palindromes.max()
end

# Run it...
low = 10 ** (numDigits - 1)
high = 10 ** numDigits
puts find_largest_palindrome_exhaustive(low, high)
