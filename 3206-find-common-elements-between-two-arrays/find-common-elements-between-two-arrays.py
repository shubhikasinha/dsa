class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        x = 0
        y = 0
        for i in nums1:
            if i in nums2:
                x = x + 1
        for j in nums2:
            if j in nums1:
                y = y + 1
        
        answer = [x, y]
        return answer        
        