class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        in_set = set()
        
        for num in nums:
            if num in in_set:
                return True
            in_set.add(num)
        return False

"""
- less efficient solution via sorting
    nums.sort()      
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True    
        return False
"""