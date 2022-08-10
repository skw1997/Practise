import sys
from collections import defaultdict, deque


class Solution():
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        dict, leng = defaultdict(list), len(quiet)
        depth = [0] * leng
        for u, v in richer:
            dict[u].append(v)
            depth[v] += 1

        q = deque([u for u in range(leng) if not depth[u]])
        ans = list(range(leng))
        while q:
            u = q.popleft()
            for v in dict[u]:
                if quiet[ans[u]] < quiet[ans[v]]:
                    ans[v] = ans[u]
                depth[v] -= 1
                if not depth[v]:
                    q.append(v)
        return ans
    #     big = [[i] for i in range(len(quiet))]
    #     res = [i for i in range(len(quiet))]
    #     for i in range(len(richer)):
    #         big[richer[i][1]].append(richer[i][0])
    #
    #     for x in range(len(big)):
    #         self.larger(big, x, x, res, quiet)
    #     return res
    #
    # def larger(self, big, oIndex, cIndex, res, quiet):
    #     if len(big[cIndex]) == 0:
    #         return
    #     for x in range(len(big[cIndex])):
    #         if big[cIndex][x] != cIndex:
    #             res[oIndex] = big[cIndex][x] if quiet[big[cIndex][x]] < quiet[res[oIndex]] else res[oIndex]
    #             self.larger(big, oIndex, big[cIndex][x], res, quiet)


s = Solution()
richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
result = s.loudAndRich(richer, quiet)
result = 0




