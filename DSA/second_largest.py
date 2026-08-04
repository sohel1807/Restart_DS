def second_largest(list):
    largest=float("-inf")
    second=float("-inf")
    
    for i in range(0,len(list)):
        if largest<list[i]:
            second=largest
            largest=list[i]
        elif list[i]<largest and list[i]>second:
            second=list[i]
            
    return second

def second_smallest(list):
    smallest=float("inf")
    second=float("inf")
    
    for i in range(0,len(list)):
        if smallest>list[i]:
            second=smallest
            smallest=list[i]
        elif list[i]>smallest and list[i]<second:
            second=list[i]
            
    return second

print(second_largest([-10,-22,-34,0,-5]))
print(second_smallest([-10,-22,-34,0,-5]))