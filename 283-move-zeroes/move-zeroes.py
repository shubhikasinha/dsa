class Solution(object):
    def moveZeroes(self, nums):
        x = len(nums)
        c = 0
        for i in range(x):
            if nums[i] != 0:
                nums[c],nums[i] = nums[i], nums[c]
                c=c+1
        return nums

        