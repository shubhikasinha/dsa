class Solution(object):
    def concatWithReverse(self, nums):
        x = nums[::-1]
        nums.extend(x)
        return nums

        