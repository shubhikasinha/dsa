# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        ans = []

        def inorder(node):
            if node is None:
                return 
            
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        inorder(root)
        inc = True
        for i in range(len(ans)-1):
            if ans[i] >= ans[i+1] :
                inc = False
        
        return inc

        

      
        