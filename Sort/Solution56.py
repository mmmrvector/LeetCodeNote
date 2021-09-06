class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        from functools import cmp_to_key
        # left = [x[0] for x in intervals]
        # right = [x[1] for x in intervals]

        def cmp(a, b):
            return a[0] - b[0]

        intervals = sorted(intervals, key=cmp_to_key(cmp))

        i = 1
        n = len(intervals)
        res = [intervals[0]]
        while i < n:
            cur_inter = res[-1]
            if cur_inter[1] >= intervals[i][0]:
                cur_inter[1] = max(cur_inter[1], intervals[i][1])
                res[-1] = cur_inter
            else:
                res.append(intervals[i])
            i += 1
        return res



s = Solution()
print(s.merge([[4,5],[3,2],[1,3]]))
