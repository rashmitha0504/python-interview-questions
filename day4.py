'''
23. 
Sum of natural numbers

n=int(input())#5 
if n<0:
    print("Enter a positive number")
else:
    sum=0 
    while(n>0):
        sum=sum+n 
        n=n-1 
    print("The sum is",sum)


24. sum of Even numbers by using while loop

n=int(input())
if n<0:
    print("Enter positive number")
else:
    sum=0 
    while(n>0):
        if n%2==0:
            sum=sum+n 
        n=n-1 
    print(sum)

    
25. HCF of Two numbers
input : 24 48
output: 24 

num_1=int(input())
num_2=int(input())
hcf=1
for i in range(1,min(num_1,num_2)+1):
    if num_1%i==0 and num_2%i==0:
        hcf=i 
print("hcf :",hcf)


26.LCM of two numbers 
input :6 8 
output : 84 

num_1=int(input())
num_2=int(input())
for i in range(max(num_1,num_2),1+(num_1*num_2)):#8,49
    if i%num_1==0 and i%num_2==0:
        lcm=i 
        break 
print("LCM :", lcm)


27. Harshad number using python 

check if the sum of the digits can
perfectly divide the number or not,
explination: 2+4=6 ,24%6==0 so harshad number

input :24
output : Harshad number

num=input()
sum=0 
for i in num:
    sum=sum+int(i)
if int(num)%sum==0:
    print("Harshad number")
else:
    print("no")

'''