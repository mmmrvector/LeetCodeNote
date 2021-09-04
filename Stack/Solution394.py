class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res = ""
        for c in s:
            if c == ']':
                value = ""
                while stack and stack[-1] != '[':
                    value = stack.pop() + value
                # pop '['
                stack.pop()
                value = int(stack.pop()) * value
                stack.append(value)


            else:
                if c.isdigit() and stack and stack[-1].isdigit():
                    stack[-1] += c
                else:
                    stack.append(c)
        return "".join(stack)

s = Solution()
print(s.decodeString("100[leetcode]"))