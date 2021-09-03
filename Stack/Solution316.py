class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i, c in enumerate(s):
            if len(stack) == 0:
                stack.append(c)
            if c in stack:
                continue
            else:
                while len(stack) != 0 and stack[-1] > c and stack[-1] in s[i + 1:]:
                    stack.pop(-1)
                stack.append(c)
        return "".join(stack)


s = Solution()
print(s.removeDuplicateLetters("bccab"))