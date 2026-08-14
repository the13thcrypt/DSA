num=1001
n= num
result=0
while n>0:
    last=n%10
    result = (result*10)+last
    n=n//10
if result==num:
    print ("the number",num,"is a palindrome")
else:
    print("the number",num,"is not a palindrome")

