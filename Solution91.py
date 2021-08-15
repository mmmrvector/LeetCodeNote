class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isValid(ss):
            if ss[0] == '0':
                return False
            if int(ss) > 26:
                return False
            return True
        n = len(s)
        res = [0] * (n + 1)
        res[0] = 1
        if isValid(s[0]):
            res[1] = 1
        else:
            res[1] = 0
        s = "0" + s
        for i in range(2, n + 1):
            if isValid(s[i]):
                res[i] += res[i - 1]
            if isValid(s[i - 1:i + 1]):
                res[i] += res[i - 2]
        return res[n]

s = Solution()
print(s.numDecodings('06'))