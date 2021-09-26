class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def dfs(num, res, n):
            for i in range(10):
                data = num * 10 + i
                if data > n:
                    break
                res.append(data)
                dfs(data, res, n)
        res = []
        for i in range(1, 10):
            if i > n:
                break
            res.append(i)
            dfs(i, res, n)
        return res