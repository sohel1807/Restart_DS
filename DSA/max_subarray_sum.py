def max_sum_subarray(list):
    max_sum=float("-inf")
    total=0
    for num in list:
        total+=num
        if total>max_sum:
            max_sum=total
        if total<0:
            total=0
    return max_sum

print(max_sum_subarray([-1,0,2,3,-1]))            