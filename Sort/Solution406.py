class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        import functools
        def mycmp(a, b):
            if a[1] != b[1]:
                return a[1] - b[1]
            else:
                return b[0] - a[0]
        # 将people 按照 k从小到大排列，若k相同，则按照h从大到小排列
        people = sorted(people, key=functools.cmp_to_key(mycmp))

        res = [people[0]]
        for p in people[1:]:
            k = 0
            for i in range(len(res)):
                if res[i][0] >= p[0]:
                    k += 1
                    if p[1] == 0:
                        res.insert(i, p)
                        break
                    if k == p[1]:
                        res.insert(i + 1, p)
                        break
            if k == 0:
                res.append(p)
        return res

s = Solution()
print(s.reconstructQueue( [[2,4],[3,4],[9,0],[0,6],[7,1],[6,0],[7,3],[2,5],[1,1],[8,0]]))