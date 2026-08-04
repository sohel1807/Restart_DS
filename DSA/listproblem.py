list=[2,3,1,3,1,3,2]
def check(list):
    map={}
    seen={}
    for number in list:
        map[number]=map.get(number,0)+1
    seen=map.copy()
    
    for i,j in map.items():
        seen.pop(i)
        if j in seen.values():
            return False
    return True    

print(check(list))    
    
