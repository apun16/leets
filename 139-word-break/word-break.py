class Solution(object):
    def wordBreak(self, s, wordDict):
        wset = set(wordDict)
        nlen = len(s)
        dp_arr = [False] * (nlen + 1)
        dp_arr[0] = True
        for end in range(1, nlen + 1):
            for start in range(end):
                if dp_arr[start] and s[start:end] in wset:
                    dp_arr[end] = True
                    break
        return dp_arr[nlen]