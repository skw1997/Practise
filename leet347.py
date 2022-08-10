import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # res = []
        # count = {}
        # for num in nums:
        #     count[num] += 1
        # freq = [[] for _ in range(len(nums))]
        # for n, f in count:
        #     freq[f].append(n)
        #
        # for i in range(len(freq)-1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res
        res = []
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        heap = []
        for key in count:
            heapq.heappush(heap, (count[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        for i in range(k-1, -1, -1):
            res.append(heapq.heappop(heap)[1])
        return res


