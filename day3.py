'''
19. Distinct characters 
input:"RASHMITHA"
output:"R A S H M I T "

s=input()
list_1=[]
for i in s:
    if i not in list_1:
        list_1.append(i)
print(" ".join(list_1))


20. List of test scores 
input :
3 4
1 2 3 4
15 10 20 5
30 18 7 16

output :
1 2 3 4 5 20 10 15 30 18 7 16

m,n=list(map(int,input().split()))
matrix=[]
for i in range(m):
    values=list(map(int,input().split()))
    matrix.append(values)

for j in range(len(matrix)):#3 0,1,2
    if j%2==1:
        for k in range(len(matrix[j])-1,-1,-1):#2,1,0
            print(matrix[j][k], end=" ")
    else:
        for k in range(len(matrix[j])):
            print(matrix[j][k],end=" ")

            
21.
input:85,88,78
      85,86,84

output:
85 85
86 88
84 78

li_1=list(map(int,input().split(",")))
li_2=list(map(int,input().split(",")))
len_li_1=len(li_1)
len_li_2=len(li_2)
for i in range(len_li_1):#0,1,2
    print(li_2[i],li_1[i])

22. 
Input : pujith long book 
output : pujith

str_1=input().split()
str_1.sort()
more_char_word=str_1[0]
char_count=len(set(str_1[0]))

for i in str_1:
    len_i=len(set(i))
    if len_i>char_count:
        more_char_word=i 
        char_count=len_i
print(more_char_word)
'''
