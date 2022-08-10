class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hashmap = {}
        # for i, n in enumerate(numbers):
        #     if target - n in hashmap:
        #         return [hashmap[target - n], i+1]
        #     hashmap[n] = i+1
        # return
        l = 1
        r = len(numbers)
        while l < r:
            while numbers[l-1] + numbers[r-1] >= target and l < r:
                if numbers[l-1] + numbers[r-1] == target:
                    return [l, r]
                r -= 1
            l += 1
        return


