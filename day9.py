#count upper and lower characters
s = "PyThOn"
upper=0
lower=0
for i in s:
    if i.isupper():
        upper+=1
    else:
        lower+=1
print(upper)
print(lower)


#remove space
s = "hello world python"
res=""
for i in s:
    if i!=" ":
        res+=i
print(res)


#anagram check
s1="listen"
s2="silent"
if sorted(s1)==sorted(s2):
    print("anagram")
else:
    print("Not an anagram")
    
#First Non-Repeating Character
s="aabbcdde"
fre={}
for i in s:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1
for i in s:
    if fre[i]==1:
        print(i)
        break
    
#Most Frequent Character
s = "banana"
fre={}
for i in s:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1
maximum=0
ans=""
for j in fre:
    if fre[j]>maximum:
        maximum=fre[j]
        answer=j
print(answer)

            
                    
s="HelloWorld"
upper=0
lower=0
for i in s:
    if i.isupper():
       upper+=1
    else:
        lower+=1
print(upper)
print(lower) 

s="my name is python"
res=""
for i in s:
    if i!=" ":
        res+=i
print(res)


s1="earth"
s2="heart"
if sorted(s1)==sorted(s2):
    print("anagram")
else:
    print("not anagram")
    
s3="aabbccddef"
fre={}
for i in s3:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1
for i in s3:
    if fre[i]==1:
        print(i)
        break