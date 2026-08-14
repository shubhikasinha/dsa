class Solution(object):
    def hasMatch(self, s, p):
        prefix, suffix = p.split('*')
        
        i = s.find(prefix)
        if i == -1:
            return False
        
        j = s.find(suffix, i + len(prefix))
        if j == -1:
            return False
            
        return True
        