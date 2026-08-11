class Solution(object):
    def isArraySpecial(self, nums):
        x = True
        if len(nums) == 1 or 0:
            return True
        for i in range(len(nums) - 1):
            if (nums[i]%2 == 0 and nums[i+1]%2 != 0) or (nums[i+1]%2 == 0 and nums[i]%2 != 0):
                x = True
            else:
                x = False
                break
        return x

        