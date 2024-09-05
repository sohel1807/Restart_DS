# def add(*args):
#     s=0
#     for i in range(len(args)):
#         s+=args[i]
#     return s
# sum=add(14,6,23,56)
# print(sum)
def printVariableAndValue(**args):
    for x in args:
        print("Variable Name :",x," value Is:",args[x])
printVariableAndValue(age="21",name="Sohel",number="34")