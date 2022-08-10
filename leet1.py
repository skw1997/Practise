class Solution():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, n in enumerate(nums):
            if target - n in hashmap:
                return [hashmap[target - n], i]
            hashmap[n] = i
        return

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,8]
    s.twoSum(nums, 9)
