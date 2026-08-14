import math
num=33
n=num
count=1
for i in range(1,num+1):
    if num%i==0:
        print(i)

#better approach only loop till half of the number
num=70
for i in range(1,num//2+1):
    if num%i==0:
        print(i)
#MOST OPTIMIZED APPROACH
from math import sqrt
num=25
result=[]
for i in range(1,int(sqrt(num))+1):
    if num%i==0:
        result.append(i)
        if i!=num//i:
            result.append(num//i)

result.sort(reverse=False)
print(result)