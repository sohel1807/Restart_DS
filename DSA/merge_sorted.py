left = [1,2,3,4,5,7]
right = [2,4,4,7,10,12,14,16,18]
def merge(left,right):
    n,m = len(left),len(right)
    result = []
    r = 0 
    i,j = 0,0 
    while i<n and j<m :
        if left[i]<=right[j]:
            if not(left[i] in result) :
                result.append(left[i])
                r += 1 
            i += 1
        else:
            if not(right[j] in result) :
                result.append(right[j])
                r += 1 
            j += 1
    while i<n : 
        if not(left[i] in result) :
            result.append(left[i])
        i += 1 
    while j<m :
        if not(right[j] in result) :
            result.append(right[j])
        j += 1 
    return result
print(merge(left,right))