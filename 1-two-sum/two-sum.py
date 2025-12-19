class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        looped = {}
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in looped:
                return [looped[complement], i]

            looped[nums[i]] = i
  
"""
A HashMap stores key → value pairs. A HashMap trades memory for speed by letting you gp directly to the data instead of searching. 

Iterate once through the array, store each numbers index in a HashMap and for each element check whether the number needed to reach the target has already been seen. If it has return the two indices.
"""