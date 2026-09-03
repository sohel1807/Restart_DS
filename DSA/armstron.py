def check(num):
    n=len(str(num))
    sum=0
    ori=num
    while num>0:
        remain=num%10
        sum+=remain**n
        num=num//10
    if sum==ori:
        return True
    return False

print(check(153))  


def revrse(num):
    sum=0
    while num>0:
        remain=num%10
        sum=sum*10+remain
        num=num//10
    return sum

print(revrse(120))    
      