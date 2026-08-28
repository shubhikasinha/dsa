class Solution(object):
    def limitOccurrences(self, nums, k):
        ans = []

        for num in nums:
            if ans.count(num) < k:
                ans.append(num)

        return ans