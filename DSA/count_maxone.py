def count_maxone(arr):
    i = 0
    maximum = 0

    for j in range(len(arr)):
        if arr[j] != 1:
            maximum = max(maximum, j - i)
            i = j + 1
            

    maximum = max(maximum, len(arr) - i)
    return maximum
print(count_maxone([1,2,0,0,1,1,0]))