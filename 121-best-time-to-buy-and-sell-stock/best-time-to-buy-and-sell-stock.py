class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        minp = prices[0]
        maxp = 0

        for price in prices[1:]:
            if price < minp:
                minp = price
            else:
                maxp = max(maxp, price - minp)

        return maxp