def count_subarrays(list):
    count=0
    for r in range(0,len(list)):
        count+=r+1
    return count

print(count_subarrays([1,2]))    