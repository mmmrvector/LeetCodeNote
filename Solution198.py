class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        max_money = [0 for _ in range(len(nums))]
        max_money[0] = nums[0]
        max_money[1] = nums[1] if nums[1] > nums[0] else nums[0]
        for i in range(2, len(nums)):
            if max_money[i - 2] + nums[i] > max_money[i - 1]:
                max_money[i] = max_money[i - 2] + nums[i]
            else:
                max_money[i] = max_money[i - 1]
        return max_money[len(nums) - 1]
s = Solution()
print(s.rob([100,1,1,100,11,1]))