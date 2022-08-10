class leet796():
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        return len(s) == len(goal) and goal in s + s


if __name__ == '__main__':
    s = leet796()
    print(s.rotateString("abcde", "cdeab"))
