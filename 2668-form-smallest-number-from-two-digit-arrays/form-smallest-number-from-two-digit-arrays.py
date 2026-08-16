class Solution(object):
    def minNumber(self, nums1, nums2):
        common_digits = set(nums1).intersection(set(nums2))
        
        if common_digits:
            return min(common_digits)
        
        min1 = min(nums1)
        min2 = min(nums2)
        
        return min(min1, min2) * 10 + max(min1, min2)