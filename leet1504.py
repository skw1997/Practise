import sys


class Solution():
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        # width = len(mat[0])
        # length = len(mat)
        #
        # rearrange = [[0]*width for i in range(length)]
        #
        # for j in range(width):
        #     for j in range(length):
        #         if mat[j][i] == 1:
        #             rearrange[j][i] = (rearrange[j][i-1] or 0) + 1
        #
        # ans = 0
        # for i in range(length):
        #     for j in range(width):
        #         minx = sys.maxsize
        #         for k in range(i, -1, -1):
        #             minx = min(rearrange[k][j], minx)
        #             ans += minx
        #             if minx == 0:
        #                 break
        # return ans
        m = len(mat)
        n = len(mat[0])

        res = 0
        height = [0] * n
        for i in range(m):
            f = [0] * n
            stack = []
            for j in range(n):
                if mat[i][j] == 0:
                    height[j] = 0
                    print(height[j], end=" ")
                elif i == 0:
                    height[j] = mat[i][j]
                    print(height[j], end=" ")
                else:
                    height[j] += mat[i][j]
                    print(height[j], end=" ")
                while stack and height[stack[-1]] >= height[j]:
                    stack.pop()

                if not stack:
                    f[j] = height[j] * (j + 1)
                    print(f[j], end="f ")
                else:
                    f[j] = f[stack[-1]] + height[j] * (j - stack[-1])
                    print(f[j], end="f ")
                res += f[j]

                stack.append(j)
            print(";")
        return res

s = Solution()
mat = [[0,1,0,1],
            [0,1,1,1],
            [1,1,1,0]]
s.numSubmat(mat)

