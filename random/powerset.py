def powerset(L):
    if len(L) == 0:
        return []
    elif len(L) == 1:
        return [[], L]
    else:
        powersets = []
        for subset in powerset(L[1:]):
            powersets.append([L[0]] + subset)
            powersets.append(subset)
        return powersets

x = powerset([])
print x, len(x)
x = powerset([1])
print x, len(x)
x = powerset([1,2])
print x, len(x)
x = powerset([1,2,3])
print x, len(x)
x = powerset([1,2,3,4])
print x, len(x)
