class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        res = []
        n = len(expression)
        for i in range(n):
            if expression[i] == '+' or expression[i] == '-' or expression[i] == '*':
                lefts = self.diffWaysToCompute(expression[:i])
                rights = self.diffWaysToCompute(expression[i + 1:])
                for l in lefts:
                    for r in rights:
                        if expression[i] == '+':
                            res.append(l + r)
                        elif expression[i] == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        if not res:
            res.append(int(expression))
        return res
s = Solution()
print(s.diffWaysToCompute("2-1-1"))