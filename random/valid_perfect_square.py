def vps(n):
    if n == 0 or n == 1:
        return 1
    if n < 0:
        return False

    low = 2
    high = n
    while low <= high:
        x = ((high - low) / 2) + low
        x2 = x * x
        if x2 > n:
            high = x - 1
        elif x2 < n:
            low = x + 1
        else:
            return True
    return False

print vps(16)
print vps(14)
print vps(0)
print vps(1)
print vps(2)