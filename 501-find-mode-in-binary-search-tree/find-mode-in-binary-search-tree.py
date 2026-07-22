# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findMode(self, root):
        ans = []
        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        inorder(root)
        counts = Counter(ans)
        max_freq = max(counts.values())
        
        return [val for val, freq in counts.items() if freq == max_freq]