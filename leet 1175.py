from math import sqrt


class Solution(object):

    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        prim = sum(self.isPrime(i) for i in range(1, n+1))
        return self.factorial(prim)*self.factorial(n-prim)%(10 ** 9 + 7)

    def isPrime(self,n):
        if n == 1:
            return 0
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return 0
        return 1

    def factorial(self, n):
        res = 1
        for i in range(1, n+1):
            res *= i
            res %= (10 ** 9 + 7)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.numPrimeArrangements(5))