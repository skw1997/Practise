from collections import deque


class Solution():
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque([root])
        ans = list()
        while q:
            level = []
            size = len(q)
            for i in range(size):
                node = q.popleft()
                level.append(node.val)
                for child in node.children:
                    q.append(child)
            ans.append(level)
        return ans

