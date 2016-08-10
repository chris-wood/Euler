def fpow(x,n):
    if n < 0:
        return fpow(1 / x, n * -1)
    if n == 0:
        return 1.0
    elif n == 1:
        return x

    product = 1.0
    while (n > 0):
        if n % 2 != 0:
            product *= x
        n /= 2
        x *= x
    return product

print fpow(2.1, 8)
print pow(2.1, 8)
print ""

print fpow(3.1, -7)
print 3.1 ** -7
print ""

# print fpow(8.84372, -5)
# print 8.84372 ** -5
# print ""

print fpow(8.66731, 4)
print pow(8.66731, 4)
print ""
