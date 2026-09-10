from collections import Counter

class Solution(object):
    def kthDistinct(self, arr, k):
        counts = Counter(arr) 
        
        for item in arr:
            if counts[item] == 1:
                k -= 1
                if k == 0:
                    return item
                    
        return ""