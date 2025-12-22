class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for c in candidates:
            for i in range(c, target + 1):
                for combination in dp[i - c]:
                    dp[i].append(combination + [c])
        
        return dp[target]