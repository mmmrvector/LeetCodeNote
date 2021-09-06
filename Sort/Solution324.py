class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        import math
        nums.sort()
        n = len(nums)
        mid = int(math.ceil(n / 2))
        n1 = nums[:mid]
        n1 = n1[::-1]
        n2 = nums[mid:]
        n2 = n2[::-1]
        i, j = 0, 0
        res = []
        while i < mid and j < n - mid:
            res.append(n1[i])
            res.append(n2[j])
            i += 1
            j += 1
        if i < mid:
            res.append(n1[i])
        for i in range(n):
            nums[i] = res[i]
        return nums
s = Solution()
print(s.wiggleSort([4,5,5,6]))