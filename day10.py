#Hash functon
s="banana"
fre={}
for i in s:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1
print(fre)
print(fre['a'])

#chec duplcates
arr=[1,2,3,4,2]
duplicate=[]
for  i in arr:
    if i in duplicate:
        print("True")
    else:
        duplicate.append(i)


#intersection of arr
a=[1,2,3]
b=[2,3,4]
set1=set(a)
result=[]
for i in b:
    if i in set1 and i not in result:
        result.append(i)
print(result)



#most frequent character.
s="mississippi"
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
        ans=j
print(ans)