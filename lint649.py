class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ''
        for str in strs:
            res += '{}:{}'.format(len(str), str)
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != ':':
                j += 1
            length = int(str[i:j])
            i = j + 1
            res.append(str[i:i+length])
            i += length
        return res
if __name__ == '__main__':
    s = Solution()
    strs = ['neet', 'code']
    en = s.encode(strs)
    print(s.decode(en))