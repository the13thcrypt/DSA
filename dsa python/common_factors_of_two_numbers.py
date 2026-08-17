from math import sqrt , gcd
a=12
b=6
cf=gcd(a,b)
count=0
for i in range(1,int(sqrt(cf))+1):
    if cf%i==0:
        count+=1
        if i!=cf//i:
            count=count+1   
print(count)             
