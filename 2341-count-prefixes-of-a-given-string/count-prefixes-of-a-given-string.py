class Solution(object):
    def countPrefixes(self, words, s):
        c = 0
        for i in words:
            if s.startswith(i):
                c +=1

        return c