class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            if target == nums[i]:
                ans.append(i)

        return ans
