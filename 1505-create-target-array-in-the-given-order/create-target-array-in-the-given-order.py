class Solution(object):
    def createTargetArray(self, nums, index):
        ans =[]
        for i in range(len(index)):
            x = index[i]
            y = nums[i]
            ans.insert(x,y)
        return ans
            