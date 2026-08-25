def func(nums , l,r):
    if l>=r:
        return
    else:
     nums[l],nums[r]=nums[r],nums[l]
     func(nums,l+1,r-1)
    
def reversearr(nums,l,r):
   func(nums,l,r)
   return nums




nums=[5,6,3,4,5,2,3,4,1]
#i only want to reverse some part of the list not the entire list
#left=2 , right=5
# left=0 , right = 9/8
'''num.reverse()
num[::-1]'''
print(reversearr(nums,0,8))

