#Finding Duplicates in array
def duplicates(arr):
    seen=set()
    duplicates=set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return duplicates

array=(1,2,1,2,1,3,4,5,5,3,6)
list=duplicates(array)
for i in list:
    print(i)
