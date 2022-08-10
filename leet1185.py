class Solution():
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        dp = [[[-1]*2*n for i in range(n)] for j in range(n)]

    def help(self, graph, step, x, y, dp):
        n = len(graph)
        if step == 2*n:
            return 0

