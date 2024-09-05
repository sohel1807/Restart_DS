#Encoding and decoding of given string
print("1)Encode\n2)Decode")
n=int(input("Enter your option from (1,2):-"))
if n==1:
    a=input("Enter string:")
    words=a.split()
    new=[]
    for x in words:
        if len(x)>=3:
            r1="hfd"
            r2="dfd"
            stnew=r1+x[1:]+x[0]+r2
            new.append(stnew)
        else:
            stnew=x[::-1]
            new.append(stnew)
    print(" ".join(new))
elif n==2:
    a=input("Enter Encoded string:")
    words=a.split()
    new=[]
    for x in words:
        n=len(x)
        if len(x)>=3:
            r1="hfd"
            r2="dfd"
            stnew=x[n-4]+x[3:n-4]
            new.append(stnew)
        else:
            stnew=x[::-1]
            new.append(stnew)
    print(" ".join(new))
    
    
       