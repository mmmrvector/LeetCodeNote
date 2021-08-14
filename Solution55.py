class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        fathest = [0] * len(nums)
        fathest[0] = nums[0]

        target = 0
        i = 0

        while i < fathest[i] and i < len(nums) - 1:
            fathest[i + 1] = max(fathest[i], nums[i + 1] + i + 1)
            i = i + 1
        for i in range(len(nums) - 1):
            if fathest[i] >= len(nums) - 1:
                return True
        return False

s = Solution()
print(s.canJump([3,2,1,0,4]))

