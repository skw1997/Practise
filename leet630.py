import heapq
import numpy as np


class Solution():
    import numpy as np
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        # c = np.array(courses)
        # d = c[np.lexsort(c.T)]
        courses.sort(key = lambda c:c[1])
        total = 0
        q = []
        for ti, di in courses:
            if total + ti <= di:
                total += ti
                # Python 默认是小根堆
                heapq.heappush(q, -ti)

            elif q and -q[0] > ti:
                total -= -q[0] - ti
                heapq.heappop(q)
                heapq.heappush(q, -ti)

        for i in range(len(q)):
            print(q[i])
        return len(q)



#超时
    # def dfs(self, courses, count, index, days, result):
    #
    #     if index == len(courses):
    #         if count > result[0]:
    #             result[0] = count
    #         return
    #
    #     if courses[index][0] + days <= courses[index][1]:
    #         #不选
    #         index += 1
    #         self.dfs(courses, count, index, days, result)
    #         index -= 1
    #
    #         #选
    #         days += courses[index][0]
    #         count += 1
    #         index += 1
    #         self.dfs(courses, count, index, days, result)
    #         index -= 1
    #         days -= courses[index][0]
    #         count -= 1
    #
    #     else:
    #         index += 1
    #         self.dfs(courses, count, index, days, result)
    #         index -= 1
    #     return result[0]

s = Solution()
courses = [[2,5],[2,19],[1,8],[1,3]]
print(s.scheduleCourse(courses))