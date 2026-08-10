#to exract digits from a number 
n=6454
num=n
while num>0:
    last_digit=num%10
    print(last_digit)
    num=num//10
