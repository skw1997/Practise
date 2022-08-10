import math
from math import atan2


class Solution():
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        """
        angles = []
        coincidence = 0
        for p in range(len(points)):
            if points[p] == location:
                coincidence += 1
            else:
                x = points[p][0] - location[0]
                y = points[p][1] - location[1]
                angles.append(atan2(y, x))

        angles.sort()
        n = len(angles)
        angles += [a + 2*math.pi for a in angles]


        inc = angle*math.pi/180
        inside = 0
        rightBound = 0
        for a in range(n):
            while rightBound < 2*n and angles[rightBound] - angles[a] <= inc:
                rightBound += 1
            inside = max(inside,rightBound-a)
        return inside+coincidence

s = Solution()
points = [[1,1],[2,2],[1,2],[2,1]]
angle = 0
location = [1,1]
print(s.visiblePoints(points, angle, location))