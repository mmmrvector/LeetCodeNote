class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        res = [ 10 ** 8 ] * (n + 1)
        res[0] = 0
        res[1] = 1
        cnt  = 0
        for i in range(2, n + 1):
            # 此处非常神器，第一种写法tle，第二种写法ac
            #for j in range(1, int((i + 2) / 2 )):
            for j in range(1, int( i ** 0.5) + 1):
                if i < j * j:
                    break
                cnt += 1
                res[i] = min(res[i], res[i - j * j] + 1)
        print(cnt)
        return res[n]
s = Solution()
print(s.numSquares(6024))
