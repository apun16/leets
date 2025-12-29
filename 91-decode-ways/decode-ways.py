class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        
        prev2, prev1 = 1, 1 
        
        for i in range(1, n):
            current = 0
            
            if s[i] != '0':
                current += prev1
            
            if i > 0 and s[i-1] != '0':
                two_digit = int(s[i-1:i+1])
                if 10 <= two_digit <= 26:
                    current += prev2
            
            prev2, prev1 = prev1, current
        
        return prev1