class Solution():
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        for i in range(len(timePoints)):
            point = timePoints[i]
            num1 = point.split(":")
            hh = int(num1[0])
            mm = int(num1[1])
            for p in timePoints[i+1:]:
                num2 = p.split(":")
                hc = int(num2[0])
                mc = int(num2[1])
                if hh > hc:
                    if hh-hc > 12:
                        hd = 24 - (hh-hc)
                        diff = abs(hd*60 + mc - mm)
                        result = diff if diff < result else result
                    else:
                        diff = abs((hh-hc) * 60 + mm - mc)
                        result = diff if diff < result else result
                else:
                    if hc-hh > 12:
                        hd = 24 - (hc-hh)
                        diff = abs(hd*60 + mm - mc)
                        result = diff if diff < result else result
                    else:
                        diff = abs((hc-hh) * 60 + mc - mm)
                        result = diff if diff < result else result
                if result == 0 :
                    return result

        return result
l = Solution()
t = ["23:59","12:00",]
print(l.findMinDifference(t))