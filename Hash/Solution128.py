class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 主要想法是要找到子序列的最小值
        HashSet = set(nums)
        max_res = 0
        for num in list(HashSet):
            cnt = 0
            tmp = num
            if num - 1 not in HashSet:
                tmp += 1
                cnt += 1
                while tmp in HashSet:
                    tmp += 1
                    cnt += 1
                max_res = max(max_res, cnt)
        return max_res