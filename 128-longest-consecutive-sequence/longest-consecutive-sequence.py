class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        nums.sort()
        maxlength = 1
        currentlength = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue 
            elif nums[i] == nums[i-1] + 1:
                currentlength += 1  
            else:
                maxlength = max(maxlength, currentlength)
                currentlength = 1
        
        return max(maxlength, currentlength)

"""
If the list is empty, there are no numbers

Longest consecutive sequence length is 0. Sorting puts numbers in increasing order to detect consecutive numbers (x, x+1). currentlength: length of the current consecutive streak, maxlength: longest streak seen so far. Both start at 1 because a single number is a streak of length. Loop through and skip duplicates. Then, if the consecutive number increases, update the current length; otherwise, reset the current length and update the max length. continue iterating till the end. 

"""