#Smallest Subarray with Sum ≥ Target
arr=[2,3,1,2,4,3]
target=7
left=0
current=0
minimum=float('inf')
for i in range(len(arr)):
    current+=arr[i]
    while current>=target:
        minimum=min(minimum,i-left+1)
        current-=arr[left]
        left+=1
print(minimum)

#Longest Substring Without Repeating Characters
s="abcabcbb"
left=0
seen=set()
maximum=0
for i in range(len(s)):
    while s[i] in seen:
        seen.remove(s[left])
        left+=1
    seen.add(s[i])
    maximum=max(maximum,i-left+1)
print(maximum)