#First Occurrence Last Occurrence
arr=[1,2,2,2,3,4,5]
target=2
left=0
right=len(arr)-1
first=-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        first=mid
        right=mid-1
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
left=0
right=len(arr)-1
last=-1

while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        last=mid
        left=mid+1
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
print(first,last)