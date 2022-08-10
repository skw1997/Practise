class ProductOfNumbers():

    def __init__(self):
        self.p = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.p = [1]
        else:
            self.p.append(self.p[-1]*num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k >= len(self.p): return 0
        print(self.p[-1])
        print(self.p[len(self.p)-k-1])
        return self.p[-1]//self.p[len(self.p)-k-1]

s = ProductOfNumbers()
s.add(3)
s.add(0)
s.add(2)
s.add(5)
s.add(4)
s.getProduct(4)
