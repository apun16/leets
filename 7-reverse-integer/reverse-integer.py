class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        s = str(abs(x))[::-1]
        res = int(s) if x >= 0 else -int(s)
        return res if -2**31 <= res <= 2**31 - 1 else 0