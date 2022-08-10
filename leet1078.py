class Solution():
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        words = text.split(" ")
        result = []
        for i in range(len(words)-2):
            if words[i] == first and words[i+1] == second:
                result.append(words[i+2])
        return result

s = Solution()
text = "we will we will rock you"
first = "we"
second = "will"
result = s.findOcurrences(text, first, second)
print(1)
