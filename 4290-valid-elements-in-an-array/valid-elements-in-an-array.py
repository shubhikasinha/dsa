class Solution(object):
    def findValidElements(self, nums):
        ans = []

        for i in range(len(nums)):
            left = nums[:i]
            right = nums[i+1:]

            if not left or nums[i] > max(left):
                ans.append(nums[i])
            elif not right or nums[i] > max(right):
                ans.append(nums[i])

        return ans
            
        