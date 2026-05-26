#Two pointers
s=list("hello")
left=0
right=len(s)-1
while left<right:
    s[left],s[right]=s[right],s[left]
    left+=1
    right-=1
print("".join(s))


# Find pair
arr=[1,2,4,5,6]
target=6
left=0
right=len(arr)-1
while left<right:
    current=arr[left]+arr[right]
    if current==target:
        print(arr[left],arr[right])
        break
    elif current<target:
        left+=1
    else:
        right-=1
        
        
#palindrome
s="medam"
left=0
right=len(s)-1
flag=True
while left<right:
    if s[left]!=s[right]:
        flag=False
        break
    left+=1
    right-=1
print(flag)



#remove duplicates
nums = [1,1,2,2,3]
k = 1
for i in range(1,len(nums)):
    if nums[i] != nums[i-1]:
        nums[k] = nums[i]
        k += 1
print(nums[:k])