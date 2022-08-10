class Solution():
    def colorBorder(self, grid, row, col, color):
        """
        :type grid: List[List[int]]
        :type row: int
        :type col: int
        :type color: int
        :rtype: List[List[int]]
        """
        if grid[row][col] == color:
            return grid
        Ocolor = grid[row][col]
        border = []
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for x in range(m)]
        self.dfs(grid,col,row,visited,Ocolor,border)
        for x,y in border:
            grid[y][x]=color
        return grid
    def dfs(self, grid, x, y, visited, Ocolor, border):
        isBorder = False
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        m, n = len(grid), len(grid[0])
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < n and 0 <= ny <m and grid[ny][nx] == Ocolor):
                isBorder = True
            elif not visited[ny][nx]:
                visited[ny][nx] = True
                self.dfs(grid,nx,ny,visited,Ocolor,border)
        if isBorder:
            border.append((x,y))

s = Solution()
grid = [[1,1],[1,2]]
s.colorBorder(grid,0,0,3)
for y in range(len(grid)):
    for x in range(len(grid[0])):
        print(grid[y][x])