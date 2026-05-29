#binary search
arr = [1,2,3,4,5,6,7]
target=5
left=0
right=len(arr)-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        print("found")
        break
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
        
#2 binary search
arr = [1,2,3,4,5,7]
target = 6
left=0
right=len(arr)-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        print("found")
        break
    elif arr[mid]<target:
        left=mid+1
    elif arr[mid]>target:
        right=mid-1
else:
    print("not found")
    
#3 Find the index
arr = [10,20,30,40,50]
target = 30
left=0
right=len(arr)-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        print(mid)
        break
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1