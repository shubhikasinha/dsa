class Solution(object):
    def sortArrayByParityII(self, nums):
        odd = []
        even = []
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)

        odd = odd[::-1]
        even = even[::-1]

        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even.pop()
            else:
                nums[i] = odd.pop()

        return nums

        