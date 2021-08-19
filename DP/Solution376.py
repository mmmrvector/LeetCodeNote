class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        dp = [0] * len(nums)
        wiggle = [0] * len(nums)
        wiggle[0] = 0
        dp[0] = 1

        for i in range(1, len(nums)):
            for j in range(i):
                if j == 0:
                    if nums[i] != nums[j]:
                        dp[i] = max(dp[i], 1 + dp[j])
                    else:
                        dp[i] = 1
                    wiggle[i] = nums[i] - nums[j]
                if wiggle[j] * (nums[i] - nums[j]) < 0:
                    dp[i] = max(dp[i], 1 + dp[j])
                    wiggle[i] = nums[i] - nums[j]
        res = 0
        for i in range(len(nums)):
            res = max(res, dp[i])
        return res
s = Solution()
print(s.wiggleMaxLength([0,0,0, 0]))