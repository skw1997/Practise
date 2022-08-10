# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        def recu(root, index):
            if len(res) == index: res.append(root.val)
            res[index] = root.val if root.val > res[index] else res[index]
            if root.left: recu(root.left, index+1)
            if root.right: recu(root.right, index + 1)
        recu(root,0)
        return res