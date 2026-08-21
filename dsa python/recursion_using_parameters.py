def func(x,n):
    if n==0:
        return
    else:
        print(x)
        func(x,n-1)

func(15,4)
'''print 1 to n using parameters'''
'''head method'''
def otn(n):
    if n==0:
        return
    else:
        otn(n-1)
        print(n)
print("second program")
otn(7)
''' tail method'''
def tn(i,n):
    if i>n:
        return
    else:
        print(i)
        tn(i+1,n)
print("tail method")        
tn(1,5)
