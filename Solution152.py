class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # f[i]表示包含nums[i]的最大乘积
        # g[i]表示包含nums[i]的最小乘积
        # 因为存在负数，有可能g[i] * nums[i] > f[i] * nums[i]，所以必须要求g[i]
        # 最大值只可能在f[i], g[i], nums[i]中间产生
        f = [0 for _ in range(len(nums))]
        g = [0 for _ in range(len(nums))]
        f[0] = nums[0]
        g[0] = nums[0]
        for i in range(1, len(nums)):
            f[i] = max(f[i - 1] * nums[i], g[i - 1] * nums[i], nums[i])
            g[i] = min(f[i - 1] * nums[i], g[i - 1] * nums[i], nums[i])
        return max(f)
s = Solution()
print(s.maxProduct([-2, 0, -1]))