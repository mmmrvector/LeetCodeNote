class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        k = int(n / 3)
        res = {}
        for num in nums:
            if num not in res:
                res[num] = 1
            else:
                res[num] += 1
        output = set()
        for num in res:
            if res[num] > k:
                output.add(num)
        return list(output)