from heapq import heappop, heappush
# class Solution(object):
#     def eatenApples(self, apples, days):
#         ans = 0
#         pq = []
#         i = 0
#         while i < len(apples):
#             while pq and pq[0][0] <= i:
#                 heappop(pq)
#             if apples[i]:
#                 heappush(pq, [i + days[i], apples[i]])
#             if pq:
#                 pq[0][1] -= 1
#                 if pq[0][1] == 0:
#                     heappop(pq)
#                 ans += 1
#             i += 1
#         while pq:
#             while pq and pq[0][0] <= i:
#                 heappop(pq)
#             if len(pq) == 0:
#                 break
#             p = heappop(pq)
#             num = min(p[0] - i, p[1])
#             ans += num
#             i += num
#         return ans

class Solution(object):
    def eatenApples(self, apples, days):
        piq = []
        i = 0
        ans = 0
        while i < len(apples):
            while piq and piq[0][0] <= i:
                heappop(piq)
            if apples[i]:
                heappush(piq,[i+days[i] , apples[i]])
            if piq:
                piq[0][1] -= 1
                if piq[0][1] == 0:
                    heappop(piq)
                ans += 1
            i += 1
        while piq:
            while piq and piq[0][0] <= i:
                heappop(piq)
            if len(piq) == 0:
                break
            p = heappop(piq)
            num = min(p[0] - i, p[1])
            ans += num
            i += num
        return ans


s = Solution()
apples = [1,2,3,5,2]
days = [3,2,1,4,2]
print(s.eatenApples(apples, days))
