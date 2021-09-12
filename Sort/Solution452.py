class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        import functools
        # 求解区间的交集
        def mycmp(a, b):
            return a[0] - b[0]

        points = sorted(points, key=functools.cmp_to_key(mycmp))
        res = [points[0]]
        i = 0
        while i < len(points):
            cur_inter = res.pop(-1)
            if cur_inter[1] < points[i][0]:
                res.append(cur_inter)
                res.append(points[i])
                i += 1
            else:
                start = points[i][0]
                end = min(points[i][1], cur_inter[1])
                res.append([start, end])
                i += 1
        return len(res)