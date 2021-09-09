class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        res = []
        for x in freq:
            res.append([x, freq[x]])
        res = sorted(res, key=lambda x: x[1], reverse=True)
        return [x[0] for x in res[:k]]

s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))