class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        n = len(nums)

        res = [[nums[0]]]
        for i in range(1, n):
            res.append([])
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(res[i]) < len(res[j]) + 1:
                        res[i] = []
                        res[i].extend(res[j])
                        res[i].append(nums[i])
            if len(res[i]) == 0:
                res[i] = [nums[i]]
        max_n = 0
        max_res = []
        for r in res:
            if max_n < len(r):
                max_n = len(r)
                max_res = r
        return max_res

s = Solution()
print(s.largestDivisibleSubset([5,9,18,54,108,540,90,180,360,720]))

