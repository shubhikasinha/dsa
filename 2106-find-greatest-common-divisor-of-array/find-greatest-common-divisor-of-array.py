class Solution(object):
    def findGCD(self, nums):
        smallest = min(nums)
        largest = max(nums)
        
        while largest % smallest != 0:
            smallest, largest = largest % smallest, smallest
            
        return smallest
        