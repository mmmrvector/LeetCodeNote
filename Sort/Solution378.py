class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        def merge(a, b):
            res = []
            while len(a) != 0 and len(b) != 0:
                if a[0] < b[0]:
                    res.append(a[0])
                    a.pop(0)
                else:
                    res.append(b[0])
                    b.pop(0)
            if len(a) != 0:
                res.extend(a)
            if len(b) != 0:
                res.extend(b)
            return res
        def mergeSort(m):
            if len(m) == 1:
                return m[0]
            if len(m) == 2:
                return merge(m[0], m[1])
            mid = int(len(m) / 2)
            return merge(mergeSort(m[:mid]), mergeSort(m[mid:]))

        res = mergeSort(matrix)
        return res[k - 1]

s = Solution()
print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
