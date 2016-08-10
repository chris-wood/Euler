import os
import random

def sub_sort(l):
    low = l[0]
    prev = -1
    index = 1
    lower_max = low
    while l[index] > low:
        prev = index
        lower_max = low
        low = l[index]
        index += 1

    low_max = prev

    high = l[-1]
    prev = -1
    index = len(l) - 2
    upper_min = high
    while l[index] < high:
        prev = index
        upper_min = high
        high = l[index]
        index -= 1

    high_min = prev

    print low_max, high_min

    prev = -1
    index = 0
    while l[index] < high_min:
        prev = index
        index += 1
    m = prev
    
    lower = l[m]
    index = high_min
    while l[index] < lower:
        index += 1
    n = index

    print m, n

    subset = l[m:n + 1]
    subset.sort()
    print subset
    return l[0:m] + subset + l[n + 1:]

l = [1,2,4,7,10,11,7,12,6,7,16,18,19]
print l
print sub_sort(l)