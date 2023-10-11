'''
1. Leap Year or not 

n=int(input())
if ((n%4==0) and (n%100!=0)) or (n%400==0):
    print("Leap Year")
else:
    print("Not a Leap Year")

    
2.count of each charcter in the word 

n=input()
n=n.lower()
unique=[]
for i in n:
    if i not in unique:
        unique.append(i)
for j in unique:
    count=n.count(j)
    print(f"{j}:{count}")

    
3.vowels check 

n=input()
vowels=['a','e','i','o','u','A','E','I','O','U']
vow_word=[]
cons_word=[]
for i in n:
    if i in vowels:
        vow_word.append(i)
    else:
        cons_word.append(i)
print(*vow_word)
print(*cons_word)


4.

*
* *
* * *
* * * *

input=int(input())
for i in range(1,input+1):
    print("* "*i)

    
5.

   *
  * *
 * * *
* * * * 

n=int(input())#4 
for i in range(1,n+1):#1,2,3,4
    spaces=" "*(n-i)
    stars="* "*i  
    print(spaces+stars)

    
6.

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


n=int(input())#5
for i in range(1,n+1):#1,2,3,4,5 
    for j in range(1,i+1):
        print(j,end=" ")
    print()

7.

1
2 3
4 5 6
7 8 9 10

n=int(input())
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1 
    print()

8.

A
B B
C C C
D D D D

n=int(input())
num=65
for i in range(1,n+1):
    for j in range(1,i+1):
        char=chr(num)
        print(char,end=" ")
    num=num+1 
    print()

9.

A
B C
D E F
G H I J 


n=int(input())
num=65 
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(num),end=" ")
        num=num+1 
    print()
'''