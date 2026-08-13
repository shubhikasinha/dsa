class Solution(object):
    def buildArray(self, nums):
        ans = []
        for i in range(len(nums)):
            x = nums[i]
            y = nums[x]
            ans.append(y)
        return ans
        