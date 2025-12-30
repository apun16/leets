class Solution(object):
    def countElements(self, nums, k):
        if k == 0:
            return len(nums)
        if not nums:
            return 0
        
        nums.sort()
        
        cutoff_index = len(nums) - k
        cutoff_value = nums[cutoff_index]

        if cutoff_value == nums[0]:
            return 0
        
        while cutoff_index >= 0 and nums[cutoff_index] == cutoff_value:
            cutoff_index -= 1
        
        return cutoff_index + 1