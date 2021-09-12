class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        median = len(nums) / 2
        if len(nums) % 2 == 0:
            median = int((nums[int(median)] + nums[int(median) - 1]) / 2)
        else:
            median = nums[int(median)]
        res = 0
        for num in nums:
            res += abs(num - median)
        return res

s = Solution()
print(s.minMoves2([1,2]))