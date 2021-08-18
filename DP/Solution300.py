class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)

        dp[0] = 1
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

s= Solution()
print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6]))