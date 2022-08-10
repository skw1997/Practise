import collections


class Solution():
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        fre = collections.Counter(s)
        for i, ch in enumerate(s):
            if fre[ch] == 1:
                return i
        return -1


