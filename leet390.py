class Solution():
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        an = 1
        k = 0
        cha = 1
        ge = n

        while ge > 1:

            k += 1
            cha << 1
            ge >> 1