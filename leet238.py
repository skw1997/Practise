class Solution():
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = 1
        res = [1] * n
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4]
    print(s.productExceptSelf(nums))
