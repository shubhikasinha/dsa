# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, target):
        new = TreeNode(target)
        if root is None:
            return new
        
        curr = root
        while curr!=None:
            if curr.val >= target:
                if curr.left != None:
                    curr = curr.left
                else :
                    curr.left = new
                    break
            if curr.val <= target:
                if curr.right != None:
                    curr = curr.right
                else :
                    curr.right = new
                    break

        return root
            

        
        