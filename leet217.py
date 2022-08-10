class Solution():
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        while nums:
            ele = nums.pop()
            if ele in nums:
                return True
        return False
if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(s.containsDuplicate(nums))