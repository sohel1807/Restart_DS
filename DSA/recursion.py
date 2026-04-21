count = 0
def fun():
    global count
    if count==4:
        return
    else:
        print("MAN")
        count+=1
        fun()

fun()      

# - Head recursion → recursive call first, work after.
# - Tail recursion → work first, recursive call last.
# 🔹 Head Recursion
# greet()
# print("hello")

# 🔹 Tail Recursion
# print("hello")
# greet()
# O(N)

# Parameter Recursion
def pfun(x,num):
    if num==0:
        return
    else:
        print(x)
        pfun(x,num-1)


pfun("saam",5) 

# Parameterized Function

def pfunction(sum,i,n):
    if i>n:
        print(sum)
        return
    pfunction(sum+i,i+1,n)


pfunction(0,1,5) 


# Functional Recursion

def frecursion(n):
    if n==1:
        return 1
    return n+frecursion(n-1)

print(frecursion(5))

# Factorial 

def factorial(n):
    if ((n==1) | (n==0)):
        return 1
    
    return n*factorial(n-1)

print(factorial(3))

# Reverse a array_number

list=[1,2,3,4,5]

def reverse(list, left=0, right=None):
    if right is None:
        right = len(list) - 1
    if left >= right:
        return list
    list[left],list[right]=list[right],list[left]
    
    reverse(list, left+1, right-1)

print(reverse(list))    