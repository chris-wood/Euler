def max_subarray(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max([arr[0], arr[1], arr[0] + arr[1]])

    sizes = [[]]
    total = 0
    start = 0
    end = 0
    max_val = 0
    count = 0

    maxes = []
    for n in arr:
        if count == 0:
            max_val = n
        elif n > max_val:
            max_val = n
    
        maxes.append(max_val)

        total += n
        sizes[start].append(total)
        count += 1

    start += 1
    end += 1

    

    # XXX: walk the upper diagonal

    #total = sum(arr)
    #total_left = sum(arr[1:])
    #total_right = sum(arr[:len(arr) - 1])
    #total_middle = max_subarray(arr[1:len(arr) - 1])
    #return max([total, total_left, total_right, total_middle])

arr = [-2,1,-3,4,-1,2,1,-5,4]
print max_subarray(arr)
