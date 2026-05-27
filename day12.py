#sliding window
arr=[2,1,5,1,3,2]
k=3
maximum=0
for i in range(len(arr)-k+1):
    current=0
    for j in range(i,i+k):
        current+=arr[j]
    maximum=max(maximum,current)
print(maximum)


#sliding window
arr=[1,4,2,10,2]
k=2
maximum=0
for i in range(len(arr)-k+1):
    current=0
    for j in range(i,i+k):
        current+=arr[j]
    maximum=max(maximum,current)
print(maximum)