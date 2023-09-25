#Here we learn about the most asked Python interview coding questions

'''
1.Reverse a String

input=input()
print(input[::-1])

or 

input=input()
empty_string=""
for i in input:
    empty_string=i+empty_string 
print(empty_string)


2.Palindrome Check 

A palindrome is a word, phrase, number, or 
other sequence of characters that reads the same forward and backward. 

n=input()
if n==n[::-1]:
    print("Palindrome")
else:
    print("No")


3.Factorial 

The factorial of a number is the product of 
all positive integers from 1 to that number.

n=int(input())
product=1 
for i in range(1,n+1):
    product=product*i 
print(product)


4.Fibonacci 

The Fibonacci sequence is a series of 
numbers in which each number (after the first two) is 
the sum of the two preceding ones. 
It typically starts with 0 and 1. Here are the first few numbers in the Fibonacci sequence:
Fibonacci series : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

#print the fibonacci of the given number 
n=int(input())
a=0 
b=1
if n<0:
    print("In correct") 
elif n==0:
    print(a)
elif n==1:
    print(b)
else:
    for i in range(1,n):
        c=a+b 
        a=b 
        b=c 
    print(b)

    (or)
    
#printing the fibonacci series to the given limit
n=int(input())
a=0 
b=1
if n==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b 
        a=b
        b=c 
        print(c)


5.anagram 

An anagram is a word or phrase formed by rearranging the letters of another word or phrase, 
typically using all the original letters exactly once. In other words, if you can rearrange the characters of 
one word to form another word, they are considered anagrams of each other.

input_1=input()
input_2=input()
input_1=input_1.replace(" ","").lower()
input_2=input_2.replace(" ","").lower()
input_1=sorted(input_1)
input_2=sorted(input_2)
if input_1==input_2:
    print("Aangram")
else:
    print("no")

    
6. Prime numbers 

#check the given number is prime or not 

n=int(input())
if n>1:
    for j in range(2,n):
        if(n%j==0):
            print("Not a Prime number")
            break
    else:
        print("Prime Number")
else:
    print("Not a Prime Number")

(AND)

#return the prime numbers in certain limit 

def is_prime(num):
    if num>1: 
        for j in range(2,num):
            if(num%j==0):
                return False    
        else:
            return True
    return True
m=int(input())
n=int(input())
for i in range(m,n+1):
    if is_prime(i):
        print(i,end=" ")



7.Armstrong

An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits. 
In other words, for an n-digit number, the sum of its digits each raised 
to the nth power is equal to the number itself.

n=input()
len_n=len(n)
count=0 
for i in n:
    count=count+int(i)**len_n
if n==str(count):
    print("Armstrong")
else:
    print("NO")


8.swap two numbers 

m=int(input())
n=int(input())
temp=m 
m=n 
n=temp 
print(m)
print(n)

(OR)

Without using 3rd variable 

a=int(input())#10
b=int(input())#5
a=a+b #15
b=a-b #15-5 10
a=a-b #15-10 5 
print(a)
print(b)

9.Perfect number

A  perfect number is a positive integer that is equal to 
the sum of its positive divisors,excluding the number itself.

n=int(input())
count=0
for i in range(1,n):
    if(n%i==0):
        count=count+i 
if count==n:
    print("Perfect")
else:
    print("No")
'''
