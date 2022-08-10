class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        width = len(grid[0])
        length = len(grid)
        widthHeight = [0]*width
        lengthHeight = [0]*length
        for i in range(width):
            for j in range(length):
                widthHeight[i] = grid[j][i] if grid[j][i] > widthHeight[i] else widthHeight[i]
                lengthHeight[j] = grid[j][i] if grid[j][i] > lengthHeight[j] else lengthHeight[j]
        ans = 0
        for i in range(width):
            for j in range(length):
                ans += widthHeight[i]- grid[j][i] if lengthHeight[j] > widthHeight[i] else lengthHeight[j] - grid[j][i]

        return ans