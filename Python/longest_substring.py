string="aaaaa"
def checksubstring(string):
    char_set=set()
    left=0
    max_length=0

    for right in range(len(string)):
        while string[right] in char_set:
            char_set.remove(string[left])
            left+=1
        char_set.add(string[right])
        max_length=max(max_length,right-left+1)

    print(max_length)

checksubstring(string)