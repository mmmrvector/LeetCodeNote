class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        import collections
        counter = collections.Counter(s)
        i = 0
        n = len(s)
        while i < n:
            c = s[i]
            if counter[c] >= k:
                i += 1
            else:
                return max(self.longestSubstring(s[: i], k), self.longestSubstring(s[i+1:], k))
        return i
s = Solution()
print(s.longestSubstring("aaabb", 3))
