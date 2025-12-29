class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [True]+[False]*n
        for i in range(1,n+1):
            for w in wordDict:
                start = i - len(w)
                if start>=0 and dp[start] and s[start:i] == w:
                    dp[i] = True
                    break
        return dp[-1]