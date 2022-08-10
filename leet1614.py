class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth = 0
        max = 0
        for x in s:
            if x == '(':
                depth += 1
                if depth > max:
                    max = depth
            elif x == ')':
                depth -= 1

        if depth > 0:
            return max - depth
        else:
            return max
