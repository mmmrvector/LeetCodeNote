class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def robb(arr):
            if len(arr) == 1:
                return arr[0]
            max_money = [0 for _ in range(len(arr))]
            max_money[0] = arr[0]
            max_money[1] = arr[1] if arr[1] > arr[0] else arr[0]
            for i in range(2, len(arr)):
                max_money[i] = max(max_money[i - 2] + arr[i], max_money[i - 1])
            return max_money[len(arr) - 1]
        if len(nums) == 1:
            return nums[0]
        return max(robb(nums[: -1]), robb(nums[1:]))
