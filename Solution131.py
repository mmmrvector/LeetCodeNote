class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        import copy
        res = []
        dp = [[False for _ in range(len(s))] for __ in range(len(s))]

        def dfs(curList, start):
            if start >= len(s):
                res.append(copy.deepcopy(curList))
            for end in range(start, len(s)):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    curList.append(s[start: end + 1])
                    dfs(curList, end + 1)
                    curList.pop(-1)
        dfs([], 0)
        return res


s = Solution()
print(s.partition("aab"))