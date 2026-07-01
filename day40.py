#All Subarrays
n=[1,2,3]
for i in range(len(n)):
    for j in range(i,len(n)):
        print(n[i:j+1])
   
#Sum of Sunarray
num=[1,2,3]
for i in range(len(num)):
    total=0
    for j in range(i,len(num)):
        total+=num[j]
        print(num[i:j+1],total)

#maximim sub array
nums = [-2,1,-3,4,-1,2,1,-5,4]
maximum=float('-inf')
for i in range(len(nums)):
    total=0
    for j in range(i,len(nums)):
        total+=nums[j]
        if total>maximum:
            maximum=total
        print(nums[i:j+1],total,maximum)
print(maximum)

#Kadane's Algorithm
nums = [-2,1,-3,4,-1,2,1,-5,4]
maximum=nums[0]
current=nums[0]
for i in range(1,len(nums)):
    current=max(nums[i],current+nums[i])
    maximum=max(maximum,current)
print(maximum)

#prefix sum
nums=[2,4,1,5,3]
prefix=[0]*len(nums)
prefix[0]=nums[0]
for i in range(1,len(nums)):
    prefix[i]=prefix[i-1]+nums[i]
print(prefix)