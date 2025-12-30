class Solution(object):
    def countElements(self, nums, k):
        n = len(nums)
        if n == 0:
            return 0
        
        sorted_nums = sorted(nums)
        count = 0
        i = 0
        
        while i < n:
            val = sorted_nums[i]
            j = i
            while j < n and sorted_nums[j] == val:
                j += 1
            
            greater_count = n - j
            
            if greater_count >= k:
                count += (j - i)
            
            i = j
        
        return count