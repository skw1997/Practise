from collections import Counter


class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        oCount = self.count(licensePlate)
        ans = None
        for word in words:
            cCount = self.count(word)
            match = True
            for i in range(26):
                if oCount[i] > cCount[i]:
                    match = False
            if match and (ans == None or len(ans) > len(word)):
                ans = word
        return ans



    def count(self, s):
        result = [0]*26
        for char in s:
            result[ord(char.lower())-ord('a')] += 1
        return result

if __name__ == '__main__':
    s = Solution()
    cnt = Counter("zzzzz")
    words = ["word", "zzzzzz"]
    for word in words:
        print(cnt - Counter(word))
    # ans = s.shortestCompletingWord("zzzzz", words)
    # print(ans)



