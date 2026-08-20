def func(x,n):
    if n==0:
        return
    else:
        print(x)
        func(x,n-1)

func(15,4)