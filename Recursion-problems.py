#1 Print 1 to N
def f(n,m):
    if n>m:
        return
    print(n)
    f(n+1,m)
f(1,10)

#2 Print N to 1
def f(n): 
    if n<=0:
        return
    print(n)
    f(n-1)
f(5) 

#3 Sum of First N Numbers
def s(n):
    if n==0:
        return 0
    return n+s(n-1)
print(s(5))

#4 factorial
def factorial(n):
    if n==1:
        return 1
    return(n*(factorial(n-1)))
print(factorial(5))

#5 power
def power(x,n):
    if n==0:
        return 1
    return x*power(x,n-1)
print(power(2,5))

#6 count Digits
def count_digts(n,count):
    if n==0:
        return count
    n=n//10 
    count+=1
    return count_digts(n,count)  
print(count_digts(123456790,0))


#7 sum of digits
def sum_digits(n,sum):
    if n==0:
        return sum
    digit=n%10
    sum+=digit
    return sum_digits(n//10,sum)
print(sum_digits(1234,0))

#8 product of digits
def product(n,p):
    if n==0:
        return p
    digits=n%10
    p*=digits
    return product(n//10,p)
print(product(1234,1))

#9 reverse Number
def reverse(n,rev):
    if n==0:
        return rev
    digit=n%10
    rev=rev*10+digit
    return reverse(n//10,rev)
print(reverse(1234,0))

#10 Check Number Palindrome
def palindrome(orginal,n,rev):
    if n==0:
        return orginal==rev
    digit=n%10
    rev=rev*10+digit
    return palindrome(orginal,n//10,rev)
print(palindrome(1221,1221,0))

#11 Reverse String
def reverse(s,left,right):
    if left>=right:
        return
    s[left], s[right]=s[right],s[left]
    reverse(s,left+1,right-1)
s=list("hello")
reverse(s,0,len(s)-1)
print("".join(s))

#12 String Palindrome
def string(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return string(s,left+1,right-1)
s=list("madam")
print(string(s,0,len(s)-1))

#13 count vowels
def vowels(s,left,count):
    if left==len(s):
        return count
    if s[left] in 'aeiouAEIOU':
        count+=1
    return(vowels(s,left+1,count))
s=list("education")
print(vowels(s,0,0))

#14 count character
def chr(s,count,left,ch):
    if left==len(s):
        return count
    if s[left]==ch:
        count+=1
    return(chr(s,count,left+1,ch))
s="banana"
ch="a"
print(chr(s,0,0,ch))

#15 remove character
def chremov(s,left,ch):
    if left==len(s):
        return s
    if s[left]==ch:
        s.remove(ch)
        return chremov(s,left,ch)
    return chremov(s,left+1,ch)
s=list("banana")
print("".join(chremov(s,0,"a")))

#16 Remove Duplicate Characters
def duplicate(s,left):
    if left==len(s):
        return ""
    if s[left] in s[:left]:
        return(duplicate(s,left+1))
    return s[left]+duplicate(s,left+1)
s=list("programming")
print(duplicate(s,0))

#17 Replace Spaces
def replace(s,left):
    if left==len(s):
        return s
    if s[left]==" ":
        s[left]="_"
    return replace(s,left+1)
s=list("Hello World")
print("".join(replace(s,0)))

#18 sum of array
def array_sum(num,left,sum):
    if left==len(num):
        return sum
    sum+=num[left]
    return array_sum(num,left+1,sum)
num=[1,2,3,4]
print(array_sum(num,0,0))

#19 Maximum Element
def max_element(num,left,max):
    if left==len(num):
        return max
    if num[left]>max:
        max=num[left]
    return(max_element(num,left+1,max))
num=[3,8,2,9,1]
max=float("-inf")
print(max_element(num,0,max))

#20 Minimum Element
def min_element(num,left,min):
    if left==len(num):
        return min
    if num[left]<min:
        min=num[left]
    return(min_element(num,left+1,min))
num=[3,8,2,9,1]
min=float("inf")
print(min_element(num,0,min))

#21 Check Sorted Array
def sorted_arr(num,left,right):
    if right==len(num):
        return True
    if num[left]>num[right]:
        return False
    return(sorted_arr(num,left+1,right+1))
num=[1,2,3,4,5]
print(sorted_arr(num,0,1))

#22. Count Even Numbers
def even_numbers(num,left,count):
    if left==len(num):
        return count
    if num[left]%2==0:
        return(even_numbers(num,left+1,count+1))
    return(even_numbers(num,left+1,count))
num=[2,5,8,9,10]
print(even_numbers(num,0,0))

#23. Count Odd Numbers
def odd_numbers(num,left,count):
    if left==len(num):
        return count
    if num[left]%2!=0:
        return(odd_numbers(num,left+1,count+1))
    return(odd_numbers(num,left+1,count))
num=[2,5,8,9,10]
print(odd_numbers(num,0,0))

#24. Linear Search
def linear_search(num,left,target):
    if left==len(num):
        return False
    if num[left]==target:
        return True
    return(linear_search(num,left+1,target))
num=[10,20,30,40]
print(linear_search(num,0,30))

#25. Binary Search
def Binary_search(num,left,right,target):
    if left>right:
        return False
    mid=(left+right)//2
    if num[mid]==target:
        return "found"
    if num[mid]<target:
        return (Binary_search(num,mid+1,right,target))
    return (Binary_search(num,left,mid-1,target))
num=[10,20,30,40,50]
print(Binary_search(num,0,len(num)-1,40))

#26. Reverse Array
def Reverse_array(num,left,right):
    if left>right:
        return num
    num[left],num[right]=num[right],num[left]
    return(Reverse_array(num,left+1,right-1))
num=[1,2,3,4]
print(Reverse_array(num,0,len(num)-1))

# 27 First Occurrence
def First_Occurrence(num,left,target):
    if left==len(num):
        return -1
    if num[left]==target:
        return left
    return(First_Occurrence(num,left+1,target))
num=[2,5,3,5,1]
print(First_Occurrence(num,0,5))

#28. Last Occurrence
def Last_occurrence(num,right,target):
    if right<0:
        return -1
    if num[right]==target:
        return right
    return Last_occurrence(num,right-1,target)
num=[2,5,3,5,1]
print(Last_occurrence(num,len(num)-1,5))

#29 Fibonacci Number
def Fibonacci_number(n):
    if n<=1:
        return n
    return Fibonacci_number(n-1)+Fibonacci_number(n-2)
print(Fibonacci_number(6))

#30 Fibonacci Series
def fib_series(n):
    if n<=1:
        return n
    return fib_series(n-1)+fib_series(n-2)
n=7
for i in range(n):
    print(fib_series(i),end=" ")
    
#31 GCD
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
print(gcd(24,18))

#32. LCM
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def LCM(a,b):
    return (a*b)//gcd(a,b)
print(LCM(4,6))

#33. Decimal to Binary
def dec_Binary(n):
    if n==0:
        return
    dec_Binary(n//2)
    print(n%2,end="")
print(dec_Binary(10))

#34 Binary to Decimal
def binary_dec(n):
    if n==0:
        return 0
    return (n%10)+2*binary_dec(n//10)
print(binary_dec(1010))