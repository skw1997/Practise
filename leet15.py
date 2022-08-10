class Solution():
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numbers = sorted(nums)
        res = []

        for i, n in enumerate(numbers):
            if i > 0 and n == numbers[i-1]:
                continue
            l, r = i+1, len(numbers)-1
            while l < r:
                sumo3 = n + numbers[l] + numbers[r]
                if sumo3 > 0:
                    r -= 1
                elif sumo3 < 0:
                    l += 1
                else:
                    res.append([n, numbers[l], numbers[r]])
                    l += 1
                    while numbers[l] == numbers[l-1] and l < r:
                        l += 1
        return res
if __name__ == '__main__':
    s = Solution()
    nums = [-1,0,1,0]
    print(s.threeSum(nums))