class Solution:
    def simplifyPath(self, path):
        names = path.split("/")
        stack = list()
        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != ".":
                stack.append(name)
        return "/" + "/".join(stack)


s = Solution()
p = "/a/./b/../..//c/"
print(s.simplifyPath(p))
