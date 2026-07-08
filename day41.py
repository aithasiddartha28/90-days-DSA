#heap sort
import heapq
nums=[10,4,7,2,15]
heapq.heapify(nums)
sorted_arr=[]
while nums:
    sorted_arr.append(heapq.heappop(nums))
print(sorted_arr)


#Recursion
def fun(n):
    if n == 0:
        return
    fun(n-1)
    print(n)
fun(5)

#factoral
def factoral(n):
    if n==1:
        return 1
    m=n*(factoral(n-1))
    return m
print(factoral(5))

#fibonacci
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(3))

#palindrome
def palindrome(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return palindrome(s, left+1, right-1)
s="madam"
print(palindrome(s,0,len(s)-1))

#reverse a string 
def reverse(s):
    if len(s)<=1:
        return s
    return reverse(s[1:])+s[0]
print(reverse("siddu"))

#power 
def power(x,n):
    if n==0:
        return 1
    return x*power(x,n-1)
print(power(2,5))

#find element in Binary search
def element(n,left,right,target):
    if left>right:
        return -1
    mid=(left+right)//2
    if n[mid]==target:
        return mid
    elif n[mid]<target:
        left=mid+1
        return element(n, left, right, target)
    else:
        right=mid-1
        return element(n,left,right,target)
n=[10,20,30,40,50]
print(element(n,0,len(n)-1,40))

#sunset
def backtrack(index):
    if index==len(nums):
        ans
        
def numbers(n):
    if n==0:
        return
    print(n)

    return numbers(n-1)

print(numbers(10))
