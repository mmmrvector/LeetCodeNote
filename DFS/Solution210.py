class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        pres = {}
        degrees = [0 for i in range(numCourses)]
        for p in prerequisites:
            if p[0] not in pres:
                pres[p[0]] = [p[1]]
                degrees[p[0]] += 1
            else:
                pres[p[0]].append(p[1])
                degrees[p[0]] += 1

        count = 0
        q = []
        res = []
        for i, d in enumerate(degrees):
            if d == 0:
                q.append(i)
        while len(q) != 0:
            v = q.pop(0)
            res.append(v)
            count += 1
            for p in pres:
                if v in pres[p]:
                    pres[p].remove(v)
                    degrees[p] -= 1
                    if degrees[p] == 0:
                        q.append(p)

        if count == numCourses:
            return res
        else:
            return []

s =  Solution()
print(s.canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))