from math import sqrt
# extraction of numbers from digit
num=6785
while(num>0):
    digit=num%10
    num=num//10
    print(digit)

# counts of digit from number
count=0
num=10000
while(num>0):
    
    count+=1
    num=num//10
    # time complexity (O(log10(n)))
print(count)    

# Check For Palindrome Number
num=5432
sum=0
while(num>0):
    remainder=num%10
    sum=sum*10+remainder
    num=num//10
    # time complexity (O(log10(n)))
print(sum)    

# Armstrong Digit 
num=1634
len_num=len(str(num))
total=0
while(num>0):
    last_digit=num%10
    total+=last_digit**len_num
    num=num//10
    # time complexity (O(log10(n)))
print(total)   

# Finding all factors Of number
num=25
result=[]
for i in range(1,int(sqrt(num))+1):
    if num%i==0:
        
        result.append(i)
        new=num//i
        if new!=i:
            result.append(new)
    # Time complexity (o(sqrt(n)))        
print(result)            


