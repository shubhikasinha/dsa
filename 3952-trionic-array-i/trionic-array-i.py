class Solution(object):
    def isTrionic(self, nums):
        n = len(nums)
        i = 0
        start = i
            
        while i < n-1 and nums[i] < nums[i+1]:
            i += 1
        
        if i == start:
            return False
        
        start = i
        while i < n-1 and nums[i] > nums[i+1]:
            i += 1
            
        if i == start:
            return False

        start = i
        while i < n-1 and nums[i] < nums[i+1]:
            i += 1
        
        if i == start:
            return False

        return i == n-1



        