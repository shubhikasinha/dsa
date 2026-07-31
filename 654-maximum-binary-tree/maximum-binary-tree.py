# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return

        maxx = nums[0]
        maxxi = 0
        for i in range(len(nums)):
            if nums[i] > maxx:
                maxx = nums[i]
                maxxi = i

        prefix = nums[0:maxxi]
        suffix = nums[maxxi+1:]

        root = TreeNode(maxx)

        root.left = self.constructMaximumBinaryTree(prefix)
        root.right = self.constructMaximumBinaryTree(suffix)
        
        return root