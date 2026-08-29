'''s='ANBCDDCBNA'
#looping
# pointers 
n=len(s)
L=0     
R=n-1
while L<R:
    if s[L]!=s[R]:
        print("false")
    L+=1
    R-=1
print("true")'''
s='saaaaaas'
L=0
R=len(s)
#USING RECURSION
def func(s,L,R):
    if L>=R:
        return True
    if s[L]!=s[R]:
        return False
    return func(s,L+1,R-1)
print(func(s,L,R-1))

