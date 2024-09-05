l=[]
x=int(input("Enter input item number: "))
for i in range(x):
    y=int(input("Enter Values: "))
    l.append(y)
# for index,value in enumerate(l):
#     print(index,value)
l.sort()
print(l)