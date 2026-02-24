class Solution:
    def twoSum(self, nums, target):
        num = {}  
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in num:
                return [num[complement], i]
            
            num[nums[i]] = i