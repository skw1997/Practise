class Solution:
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        split =s.split(" ")
        return split[:k]
l = Solution()
print(l.truncateSentence("sqw wqs qwqs", 3))


