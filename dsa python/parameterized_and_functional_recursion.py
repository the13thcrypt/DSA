'''sum of 1 to n parameterized'''
def func(total,i,n):
    if i>n:
        print(total)
        return
    func(total+i,i+1,n)
func(0,1,4)    
'''functional method'''
def funf(n):
    if n==1:
        return 1   
    return n + funf(n-1)
print("second")
print(funf(10))
