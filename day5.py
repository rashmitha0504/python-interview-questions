'''
28.
having only uppercase or lowercase or digits in string
input : Rashmitha 
output : true 

input :is evry
output : false

S=input()
ex=""
for i in S:
    if i.isupper() or i.islower() or i.isdigit():
        ex=ex+i 
if ex==S:
    print("true")
else:
    print("false")

(OR)

S=input()
ex=""
for i in S:
    if (65<=ord(i)<=90) or (97<=ord(i)<=122) or (48<=ord(i)<=57):
        ex=ex+i 
if ex==S:
    print("true")
else:
    print("false")

###############################
    
29.
dictionary order
input : Fools rush in where angels fear to tread
output : angels where

n=input().split()
first=n[0]
last=n[-1]
for i in n:
    if i.lower()<first.lower():
        first=i 
    elif i.lower()>last.lower():
        last=i 
print(first+" "+last)

################################

30.

Armstrong in given numbers 
input : 
4
8 27 153 379
output:
8 153 

n=int(input())
li=[]
for i in range(1,n+1):#1,2,3,4 
    x=input()
    li.append(x)#8,27,153,374 
    
li_2=[]
for i in li:#153
    sum=0
    length=len(i)#3
    for j in i:#1 
        y=int(j)**length
        sum=sum+y  
    if sum==i:
        li_2.append(sum)
print(li_2)

################################
31. 
input: 
5
10 11 7 12 14

output : 7 
Explination : higghest -lowest 
                14-7 

n=int(input())
li=[]
for i in range(n):
    x=int(input())
    li.append(x)
li.sort()
print(li[-1]-li[0])


################################
32.
input:
5
18 11 27 12 14 
output:
5
explination: 
18 - 1
11 - 0
27 - 2
12 - 1
14 - 1
so,total 5

n=int(input())
li=[]
for i in range(n):
    x=int(input())
    li.append(x)

sum=0
for j in li:
    x=j//12
    sum=sum+x 
print(sum) 

'''


