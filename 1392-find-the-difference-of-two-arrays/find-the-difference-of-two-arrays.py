class Solution(object):
    def findDifference(self, nums1, nums2):
        answer = []
        fhalf = []
        shalf = []
        for i in nums1:
            if i not in nums2 and i not in fhalf:
                fhalf.append(i)
                    
        for j in nums2:
            if j not in nums1 and j not in shalf:
                shalf.append(j)

        answer = [fhalf , shalf]

        return answer

                