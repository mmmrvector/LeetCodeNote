class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        import functools
        return str(int("".join(sorted([str(i) for i in nums], key=functools.cmp_to_key(lambda x,y :1 if x + y >= y + x else -1), reverse=True))))

s = Solution()
print(s.largestNumber([10,3,2]))