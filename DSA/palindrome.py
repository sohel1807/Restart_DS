def palindrome(left,r,str):
    if left>=r:
        return True
    if str[left]!=str[r]:
        return False
    return palindrome(left+1,r-1,str)
str="bac"
print(palindrome(0,len(str)-1,str))


def fibonaci(num):
    if num == 0 or num == 1:
        return num
    return fibonaci(num - 1) + fibonaci(num - 2)

n = 10

for i in range(n):
    print(fibonaci(i), end=" ")