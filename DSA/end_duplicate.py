def end_duplicate(list):
    n=len(list)
    i=0
    for j in range(len(list)):
        if list[i]!=list[j]:
            i+=1
            list[i],list[j]=list[j],list[i]
    return list,i        
            
            
print(end_duplicate([1,1,3,3,4,5]))            