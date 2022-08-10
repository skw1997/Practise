class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = True

        max_length = 1
        begin = 0

        for L in range(2,n+1):
            for i in range(n):
                j = L + i - 1

                if j > n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

            if dp[i][j] and j - i + 1 > max_length:
                max_length = j - i + 1
                begin = i
        return s[begin:begin+max_length]
