class Solution(object):
    def intersection(self, nums):
        ans = []
        for i in nums[0]:
            present = True
            for j in nums:
                if i not in j:
                    present = False
                    break

            if present==True:
                ans.append(i)

        return sorted(ans)
        