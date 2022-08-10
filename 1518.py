import math


class Solution():
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        res = numBottles
        while numBottles != 0:
            exchange = int(numBottles/numExchange)
            if exchange != 0:
                numBottles = exchange + numBottles % numExchange
            else:
                numBottles = 0
            res += exchange
        return res

s = Solution()
print(s.numWaterBottles(15,4))