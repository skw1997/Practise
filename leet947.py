class Solution():
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        n = len(stones)
        set = djset(n)
        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    set.union(i,j)
        return n - set.cnt
class djset:
    def __init__(self, M):
        self.parent = {}
        self.cnt = 0
        self.rank = {}
        for i in range(M):
            self.parent[i] = i
            self.rank[i] = 0
            self.cnt += 1

    def find_root(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find_root(self.parent[x])
            return self.parent[x]
        return x

    def union(self,x,y):
        if self.find_root(x) == self.find_root(y): return
        x_root = self.find_root(x)
        y_root = self.find_root(y)
        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        elif self.rank[y_root] > self.rank[x_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[x_root] = y_root
            self.rank[y_root] += 1
        self.cnt -= 1
if __name__ == '__main__':
    s = Solution()
    stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    print(s.removeStones(stones))