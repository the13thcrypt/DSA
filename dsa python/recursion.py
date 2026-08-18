
#print name n times
# #tail recursion
count=0
def tail():
    global count
    if count==5:
        return
    count+=1
    tail()
    print("sam will be printed 5 times") 
tail()
#head recursion
count =0 
def head():
     global count
     if count==5:
        return
    
     count+=1
     head()
     print("head function will be printed 5 times")
head()    

'''you need to draw a recursion tree for the above two functions to understand the difference between head and tail recursion. In tail recursion, the recursive call is the last statement in the function, while in head recursion, the recursive call is made before any other statements. This means that in tail recursion, the function can return immediately after the recursive call, while in head recursion, the function must wait for all recursive calls to complete before it can return.'''