n=9
def func(num):
    if num==0 or num==1:
        return num
    return func(num-1)+func(num-2)
def fib(n):
    answer=func(n)
    return answer
print(fib(n))
