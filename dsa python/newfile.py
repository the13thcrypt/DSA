nums=[3,2,1,4,5,3,2,1,2,6,4,2,1,7,11]
def merge_sort(nums):
    result=[]
    i,j=0
    n,m=len(left),len(right)
    while i<n and j<m:
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while    
