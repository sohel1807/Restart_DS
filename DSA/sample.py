# sample_str="The quick brown fox jumps over the lazy dog"

# letters=set()
# for c in sample_str.lower():
#     if c.isalpha():
#         letters.add(c)

# if len(letters)==26:
#     print(letters)
#     print("all present")  

# else:  
#      print("all not present")         
    

# list1=[1,3,5]
# list2=[2,4]
# list3=[]
# i,j=0,0
# while i<len(list1) and j<len(list2):
#     if list1[i]<=list2[j]:
#         list3.append(list1[i])
#         i+=1
#     else:
#         list3.append(list2[j])
#         j+=1


# print(list3)
# s1="listen"
# s2="silent"

# if sorted(s1.lower())==sorted(s2.lower()):
#     print("OK")
# else:
#     print("not ok")

# def first_duplicate(arr):
#     seen = {}
#     for i in range(len(arr)):
#         if arr[i] in seen:
#             print(seen)
#             return seen[arr[i]]  # Return index of FIRST occurrence
#         seen[arr[i]] = i
#     return -1

# print(first_duplicate([1,2,3,4,5,3]))  


def count_char(s, char):
    # Just count how many times char appears in s
    count = 0
    # Write simple loop here
    for c in s:
        if char==c:
            count+=1
    
    return count

# Test
print(count_char("hello", "l")) 