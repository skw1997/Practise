class Solution():
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        a = [1,2,3,4]
        arr.sort()
        diff = arr[1] - arr[0]
        result = [[arr[0], arr[1]]]
        for i in range(1, len(arr) -1):
            ndiff = arr[i+1] - arr[i]
            if ndiff < diff:
                diff =ndiff
                result = [[arr[i], arr[i+1]]]
            elif ndiff == diff:
                result.append([arr[i], arr[i+1]])
            else:
                pass
        return result
if __name__ == '__main__':
    s = Solution()
    s.minimumAbsDifference([4,2,1,3])