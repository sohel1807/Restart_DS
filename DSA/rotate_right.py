def rotate_right(list):
    n=len(list) 
    list[:]=[list[n-1]]+list[0:n-1]
    return list

print(rotate_right([1,2,3,4,5]))

def rotate_ri(list):
    n= len(list)
    temp=list[n-1]
    for i in range(n-2,-1,-1):
        list[i+1]=list[i]
        
    list[0]=temp
    
    return list

print(rotate_ri([1,2,3,4,5]))  

def rotate_k(k,list):
    n=len(list)
    k=k%n
    list[:]=list[n-k:]+list[0:n-k]
    return list

print(rotate_k(2,[1,2,3,4,5]))  