class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        while (k!=0):
            x = min(nums)
            y = nums.index(x)
            ans = x * multiplier
            nums[y] = ans
            k = k-1
        return nums
            

        