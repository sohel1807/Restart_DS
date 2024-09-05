# Enter your code here. Read input from STDIN. Print output to STDOUT
def check(number):
    result="NO"
    if number.isdigit() and len(number) ==10:
        if (number[0]=="7")or(number[0]=="8")or(number[0]=="9"):
            result="YES"
    return result
x=int(input())
for i in range(x):
    y=input()
    print(check(y))
    