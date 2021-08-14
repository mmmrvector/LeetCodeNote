class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_steps = [10 ** 8] *  len(nums)
        min_steps[0] = 0
        def dp(i):
            thresh = min_steps[i - 1]
            for j in range(i - 1, -1, -1):
                if min_steps[j] < thresh-1:
                    break
                if nums[j] >= i - j:
                    if min_steps[j] + 1 < min_steps[i]:
                        min_steps[i] = min_steps[j] + 1
        for i in range(1, len(nums)):
            dp(i)
        print(min_steps[-1])
        return min_steps[-1]

s = Solution()
s.jump([2,3,1,1,4])