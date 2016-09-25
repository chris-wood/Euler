def perm(L):
    if len(L) <= 1:
        return L
    elif len(L) == 2:
        return [ L, [L[1], L[0]] ]
    else:
        perms = []
        for p in perm(L[1:]):
            for j in range(len(p)):
                permutation = p[:]
                permutation.insert(j, L[0])
                perms.append(permutation)
            perms.append(p + [L[0]])
        return perms

print perm([1])
print perm([1,2])
print perm([1,2,3])
print perm([1,2,3,4])
x = perm([1,2,3,4])
print len(x)
