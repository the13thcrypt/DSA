n=5765
num=n
c=0
while num>0:
    last_digit=num%10
    num=num//10
    c=c+1
print("the count is",c)
#another approach (log based) the number of digits is log(n)+1
from math import log10
n=5765
def count_digits(num):
    return int(log10(num))+1
print("the count using log is ",count_digits(n))

