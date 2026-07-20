class Solution(object):

    def height(self, root):
        if root is None:
            return 0

        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root):
        if root is None:
            return True

        leftheight = self.height(root.left)
        rightheight = self.height(root.right)

        if abs(leftheight - rightheight) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)