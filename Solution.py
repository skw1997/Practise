class Solution:
    def inorderTraversal(self, root):
        list = []

        self.inorderTraversal(root.left)
        list.append(root)
        self.inorderTraversal(root.right)

        return list

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right