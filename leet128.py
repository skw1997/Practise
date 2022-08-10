class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)
#         n = len(nums)
#         set = djset(n)
#         for i in range(n):
#             for j in range(i+1, n):
#                 if abs(nums[i] - nums[j]) < 2:
#                     set.union(i,j)
#
# class djset:
#     def __init__(self, M):
#         self.parent = {}
#         self.cnt = 0
#         self.rank = {}
#         for i in range(M):
#             self.parent[i] = i
#             self.rank[i] = 0
#             self.cnt += 1
#
#     def find_root(self,x):
#         if x != self.parent[x]:
#             self.parent[x] = self.find_root(self.parent[x])
#             return self.parent[x]
#         return x
#
#     def union(self,x,y):
#         if self.find_root(x) == self.find_root(y): return
#         x_root = self.find_root(x)
#         y_root = self.find_root(y)
#         if self.rank[x_root] > self.rank[y_root]:
#             self.parent[y_root] = x_root
#         elif self.rank[y_root] > self.rank[x_root]:
#             self.parent[x_root] = y_root
#         else:
#             self.parent[x_root] = y_root
#             self.rank[y_root] += 1
#         self.cnt -= 1
