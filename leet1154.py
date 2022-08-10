import time
class Solution():
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        # days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        #
        # year, month, day = date.split("-")
        # year = int(year)
        # month = int(month)
        # day = int(day)
        #
        # if month > 1:
        #     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        #         days[1] = 29
        #
        # prev = 0
        # for i in range(month - 1):
        #     prev += days[i]
        #
        # return prev + day
        return time.strptime(date, "%Y-%m-%d")[-2]


s = Solution()
print(s.dayOfYear("2004-03-01"))

