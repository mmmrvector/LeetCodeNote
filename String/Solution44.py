class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import copy
        new_p = ""
        for i, pp in enumerate(p):
            if i == 0 or (p[i] != p[i - 1]) or(p[i] == p[i - 1] and p[i] != "*"):
                new_p += pp
        p = new_p
        memo = {}
        def match(s, p):
            if len(s) == 0:
                if p == "*" or p == "":
                    return True
                else:
                    return False
            if len(p) == 0:
                return False
            if s +'-' + p in memo:
                return memo[s +'-' + p]

            if p[-1] == s[-1] or p[-1] == "?":
                return self.isMatch(s[:-1], p[:-1])
            if p[-1] != "*":
                return False
            for i in range(len(s) + 1):
                if self.isMatch(s[:i], p[:-1]):
                    memo[s + '-' + p] = True
                    return True
            memo[s + '-' + p] = False
            return False
        return match(s, p)
s = Solution()
print(s.isMatch("abcabczzzde","*abc???de*"))