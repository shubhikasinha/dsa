class Solution(object):
    def percentageLetter(self, s, letter):
        count = 0
        l = len(s)
        for i in s:
            if i == letter:
                count = count + 1
                
        ans = (count * 100) / l
        return ans
        