class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            need=target-nums[i]
            if(need in nums and nums.index(need)!=i):
                return [i,nums.index(need)]
                
