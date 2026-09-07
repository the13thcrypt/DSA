nums=[4,5,6,7,3,4,2,4,7,5]
def sortfunc(nums):
    n=len(nums)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if nums[j]<nums[min_index]:
                min_index=j
        nums[i],nums[min_index]=nums[min_index],nums[i]
sortfunc(nums)
print(nums)            
def reverse_sort(nums):
    n=len(nums)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if nums[j]>nums[min_index]:
                min_index=j
        nums[i],nums[min_index]=nums[min_index],nums[i]
reverse_sort(nums)
print(nums)
this will later be deleted 
