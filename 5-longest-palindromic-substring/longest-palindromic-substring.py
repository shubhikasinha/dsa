class Solution(object):
    def longestPalindrome(self, s):
        longest = ""

        for i in range(len(s)):
            for j in range(i + len(longest) + 1, len(s) + 1):
                sub = s[i:j]

                if sub == sub[::-1]:
                    longest = sub

        return longest