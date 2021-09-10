class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        import functools
        n = len(intervals)
        if n == 1:
            return 0
        def mycmp(a, b):
            if a[0] != b[0]:
                return a[0] - b[0]
            else:
                return b[1] - a[1]
        intervals = sorted(intervals, key=functools.cmp_to_key(mycmp))
        i, j = 0, 1
        new_intervals = []
        while i < n - 1 and j < n:
            if intervals[i][0] < intervals[j][0]:
                new_intervals.append(intervals[i])
            i += 1
            j = i + 1
        new_intervals.append(intervals[-1])
        intervals = new_intervals
        # 去掉最少的区间，相当于找到最长无交集的区间集
        #  longest non-overlapping intervals
        m = len(intervals)
        if m == 1:
            return n - 1
        i, j = 0, 1
        ans = 0
        while i < m - 1 and j < m:
            if intervals[i][1] > intervals[j][0]:
                if intervals[i][1] <= intervals[j][1]:
                    ans += 1
                    j += 1
                else:
                    ans += 1
                    i = j
                    j = i + 1
            else:
                i = j
                j = i + 1
        return n - m + ans





s = Solution()
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))