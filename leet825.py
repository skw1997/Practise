class Solution():
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        result = 0
        ages.sort(reverse = True)
        for i in range(len(ages)):
            j = i + 1
            while j < len(ages):
                if ages[j] <= ages[i]/2 + 7:
                    j += 1
                    continue
                else:
                    if ages[i] == ages[j]:
                        result += 2
                    else:
                        result += 1
                    j += 1

        return result

s = Solution()
ages = [16,16]
print(s.numFriendRequests(ages))

