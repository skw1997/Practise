class Solution():
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        f = [[[0]*4 for i in range(110)]for j in range(n+1)]
        f[0][0][0] = 1
        for i in range(1, n+1):
            t = nums[i-1]
            for j in range(0, 110):
                for k in range(0, 4):
                    f[i][j][k] += f[i-1][j][k]
                    if j - t >= 0 and k - 1 >= 0:
                        f[i][j][k] += f[i-1][j-t][k-1]
        ans = 0
        for i in range(3, n):
            ans += f[i][nums[i]][3]
        return ans

s = Solution()
nums = [1,1,1,3,5]
print(s.countQuadruplets(nums))