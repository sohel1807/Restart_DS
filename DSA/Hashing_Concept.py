# Hashing in python
# prestoring values in some in datastructure like dict/set/list and fetching it.

n=[3,4,6,1,7,0,2,3,8,1]
m=[10,1,2,1,9,7,2,6]
dict={}
hash_list=[0]*11

for num in n:
   hash_list[num]+=1 

for num in m:
   dict[num]=hash_list[num]
   # Time Complexity O(M+N)
print(dict)


hash_map={}
for i in n:
   hash_map[n[i]]=hash_map.get(n[i],0)+1

for i in m:
   print(hash_map.get(i,0))
   

# character hashing

s = "AaYYx#@$aaaaa"
q = ['d','A','x','$']

hash_dict = {}

for ch in s:
     hash_dict[ch] = hash_dict.get(ch,0)+1

for ch in q:
     print(hash_dict.get(ch,0))
  
  