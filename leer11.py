class Solution():
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxV = 0
        maxr = len(height) - 1
        for l in range(len(height) - 1):
            r = len(height) - 1
            while l < r :
                if height[r] < height[maxr]:
                    pass
                if ((r-l) * min(height[l], height[r])) > maxV:
                    maxV = ((r-l) * min(height[l], height[r]))
                    maxr = r
                r -= 1
        return maxV
if __name__ == '__main__':
    s = Solution()
    height = [1,2,3,4,5,25,24,3,4]
    print(s.maxArea(height))