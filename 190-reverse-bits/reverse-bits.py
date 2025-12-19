class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = format(n, '032b')  
        reverse = binary[::-1]
        
        return int(reverse, 2)      