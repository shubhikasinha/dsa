class Solution(object):
    def halvesAreAlike(self, s):
        s = s.lower()
        l = len(s) / 2
        s1 = s[:l]
        s2 = s[l:]
        c1 = 0
        c2 = 0
        for i in s1:
            if i in 'aeiou' :
                c1 += 1
        
        for i in s2:
            if i in 'aeiou' :
                c2 += 1
        
        if c1 == c2:
            return True
        else:
            return False