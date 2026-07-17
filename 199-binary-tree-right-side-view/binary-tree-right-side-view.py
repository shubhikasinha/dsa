# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        ans = []
        q = deque([root])

        while q:
            level = []
            size = len(q)

            while size:
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                size -= 1

            ans.append(level)
            x = len(ans)
            anss =[]
            for i in range(x):
                anss.append(ans[i][-1])
        return anss
        
        