class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            need=target-nums[i]
            if(need in nums and nums.index(need)!=i):
                return [i,nums.index(need)]
#brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return[i,j]
#hash table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=dict()
        for i in range(len(nums)):
            d[nums[i]]=i
            for j in range(len(nums)):
                need=target-nums[j]
                if(need in d.keys() and d[need]!=j):
