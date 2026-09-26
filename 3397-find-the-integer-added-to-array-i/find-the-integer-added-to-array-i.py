class Solution(object):
    def addedInteger(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        x = nums2[0] - nums1[0]
        y = nums2[-1] - nums1[-1]
        if x==y:
            return x