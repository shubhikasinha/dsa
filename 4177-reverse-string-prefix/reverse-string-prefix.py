class Solution(object):
    def reversePrefix(self, s, k):
        x = s[:k]
        x = x[::-1]
        s = s[k:]
        s = x + s
        return s   