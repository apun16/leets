class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        binary = format(n, '032b')  
        return binary.count('1')   
