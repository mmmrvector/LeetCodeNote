class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()

        return ' '.join(list(reversed(words)))
s = Solution()
print(s.reverseWords( "the sky is blue"))