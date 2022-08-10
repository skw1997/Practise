class Solution():
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9+7
        dp =[[[0,0,0],[0,0,0]] for i in range(n+1)]
        dp[0][0][0] = 1
        for i in range(1, n+1):
            for j in range(0, 2):
                for k in range (0, 3):
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k]) % mod

            for k in range(0, 3):
                dp[i][1][0] = (dp[i][1][0] + dp[i-1][0][k]) % mod

            for j in range(0, 2):
                for k in range(1, 3):
                 dp[i][j][k] = (dp[i][j][k] + dp[i-1][j][k-1]) % mod

        total = 0
        for j in range(0, 2):
            for k in range(0, 3):
                total += dp[n][j][k]
        return total % mod
if __name__ == '__main__':
    s = Solution()
    print(s.checkRecord(10101))