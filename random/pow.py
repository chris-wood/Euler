class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        flip = n < 1
        n = abs(n)

        if n == 0:
            return 1.0
        if n == 1:
            return x if not flip else 1/x

        product = 1.0
        while n > 0:
            if n % 2 != 0:
                product *= x
            n /= 2
            x *= x
        return product if not flip else 1 / product

s = Solution()
print s.myPow(2.1, 8)
print pow(2.1, 8)
print ""

print s.myPow(3.1, -7)
print 3.1 ** -7
print ""

# print s.myPow(8.84372, -5)
# print 8.84372 ** -5
# print ""

print s.myPow(8.66731, 4)
print pow(8.66731, 4)
print ""
