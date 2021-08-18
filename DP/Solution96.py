class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [-1] * (n +1)
        def f(arr):

            if res[len(arr)] != -1:
                return res[len(arr)]

            if len(arr) == 0:
                res[0] = 0
                return 0

            if len(arr) == 1:
                res[1] = 1
                return 1

            cnt = 0
            for i, item in enumerate(arr):
                leftTrees = f(arr[0:i])
                rightTrees = f(arr[i +1: ])
                if leftTrees == 0:
                    cnt += rightTrees
                    continue
                if rightTrees == 0:
                    cnt += leftTrees
                    continue

                cnt += leftTrees * rightTrees
            res[len(arr)] = cnt
            return cnt
        return f(list(range(1, n + 1)))
s = Solution()
print(s.numTrees(3))