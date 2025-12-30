class Solution(object):
    def countElements(self, nums, k):
        n = len(nums)
        if n == 0:
            return 0
        if k == 0:
            return n
        
        nums.sort()
        count = 0
        i = 0
        
        while i < n:
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1
            
            greater_count = n - j            
            if greater_count >= k:
                count += (j - i)
            i = j
        
        return count