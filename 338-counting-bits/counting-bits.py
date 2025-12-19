class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        arr = [0] * (n + 1)
        
        for i in range(1, n + 1):
            arr[i] = arr[i // 2] + (i % 2)
        
        return arr