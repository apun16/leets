class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n_len = len(nums)
        total = n_len * (n_len + 1) // 2

        return total - sum(nums)