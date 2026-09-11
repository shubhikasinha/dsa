class Solution(object):
    def firstPalindrome(self, words):
        x =""
        for i in words:
            if i == i[::-1]:
                x = i
                return x 
        return x
        
        