class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_sub = 0
        looped = {}
        start = 0

        for end, char in enumerate(s):
            if char in looped and looped[char] >= start:
                start = looped[char] + 1

            looped[char] = end
            longest_sub = max(longest_sub, end - start + 1)

        return longest_sub

"""
TYPE: sliding window algorithm
https://www.geeksforgeeks.org/dsa/window-sliding-technique/

Scan string from start to end and store last index where each character appeared. If a character repeats inside the current window, the start is moved just past the previous occurrence to maintain uniqueness. At each step, the code updates the maximum substring length found so far.
"""