nums=[1,2,3,4,5,6,5,6,44,3,43,32,4,2,3,2,1,3,4,5,3,2,24,4,2,1]
freq=dict()
x=1
for i in range(len(nums)):
    if nums[i] in freq:
        freq[nums[i]]+=1
    else:
        freq[nums[i]]=1
    print(freq[x])