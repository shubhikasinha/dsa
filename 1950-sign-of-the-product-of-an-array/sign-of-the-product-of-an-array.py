class Solution(object):
    def arraySign(self, nums):
        if 0 in nums:
            return 0
        countn = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                countn += 1
        if countn%2 == 0:
            return 1
        else:
            return -1
        