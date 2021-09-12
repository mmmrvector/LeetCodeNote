class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        import functools
        # 按区间左端点从小到大排序
        def mycmp(a, b):
            return a[1][0] - b[1][0]
        # 按区间右端点从小到大排序
        def mycmp2(a, b):
            return a[1][1] - b[1][1]

        def mycmp3(a, b):
            return a[0] - b[0]

        new_intervals = sorted([[i, inter] for i, inter in enumerate(intervals)], key=functools.cmp_to_key(mycmp))
        raw_intervals = sorted([[i, inter] for i, inter in enumerate(intervals)], key=functools.cmp_to_key(mycmp2))
        res = []
        j = 0
        for i, inter in enumerate(raw_intervals):
            if j < len(intervals) and inter[1][1] <= new_intervals[j][1][0]:
                res.append([inter[0], new_intervals[j][0]])
            else:
                while True:
                    j = j + 1
                    if j >= len(intervals):
                        break
                    if inter[1][1] <= new_intervals[j][1][0]:
                        res.append([inter[0], new_intervals[j][0]])
                        break
                if len(res) <= i:
                    res.append([inter[0], -1])

        res = sorted(res, key=functools.cmp_to_key(mycmp3))
        return [data[1] for data in res]
