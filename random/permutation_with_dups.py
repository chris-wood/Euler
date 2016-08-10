def perm(L):
    def inner_perm(L):
        pass

    Lp = L[:]
    Lp.sort()
    
    return inner_perm(Lp)

print perm([1,2,2,3])