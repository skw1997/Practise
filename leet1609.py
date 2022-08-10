class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        cur = [root]
        level = 0
        while cur:
            nxt = []
            prev = 0
            for node in cur:
                if level % 2 + node.val == 1:
                    if prev == 0 or (prev != 0 and ((level % 2 == 0 and node.val % 2 == 1 and node.val > prev) or (level % 2 == 1 and node.val % 2 == 0 and node.val < prev))):
                        prev = node.val
                        if node.left:
                            nxt.append(node.left)
                        if node.right:
                            nxt.append(node.right)
                else:
                    return False
            level += 1
            cur = nxt
        return True
