class Solution(object):
    def longestPalindrome(self, s):
        if not s: return ""
        start, max_len = 0, 1
        
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        
        for i in range(len(s)):
            len1 = expand(i, i)
            len2 = expand(i, i + 1)
            cur_max = max(len1, len2)
            if cur_max > max_len:
                max_len = cur_max
                start = i - (cur_max - 1) // 2
        
        return s[start:start + max_len]