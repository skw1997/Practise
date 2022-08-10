from collections import defaultdict


class Solution():
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(lambda :[])

        for string in strs:
            key = sorted(string)
            res[tuple(key)].append(string)
        return res.values()
        # res = defaultdict(list)
        #
        # for string in strs:
        #     count = [0]*26
        #     for char in string:
        #         count[ord(char) - ord('a')] += 1
        #     res[tuple(count)].append(string)
        #
        # return res.values()
if __name__ == '__main__':
    strs = ['eat']
    s = Solution()
    print(s.groupAnagrams(strs))