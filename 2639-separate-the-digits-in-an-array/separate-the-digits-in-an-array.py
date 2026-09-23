class Solution(object):
    def separateDigits(self, nums):
        answer = []
        for i in range(len(nums)):
            digits = []
            digits = [int(x) for x in str(nums[i])]
            answer.extend(digits)
        return answer
        