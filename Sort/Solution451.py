class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        import functools
        map = {}
        for ss in s:
            if ss not in map:
                map[ss] = 1
            else:
                map[ss] += 1

        l = []
        for key in map:
            l.append([key, map[key]])

        def mycmp(a, b):
            return a[1] - b[1]

        l = sorted(l, key=functools.cmp_to_key(mycmp), reverse=True)
        res = ""
        for ss in l:
            res += ss[0] * ss[1]
        return res


