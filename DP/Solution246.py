class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        res = [1]
        i,j,k = 0,0,0
        l1 = [2]
        l2 = [3]
        l3 = [5]
        while len(res) < n:
            now = min(l1[i], l2[j], l3[k])
            res.append(now)
            if now == l1[i]:
                i += 1
                l1.append(res[i] * 2)
            if now == l2[j]:
                j += 1
                l2.append(res[j] * 3)
            if now == l3[k]:
                k += 1
                l3.append(res[k] * 5)
        return res[n - 1]
s = Solution()
print(s.nthUglyNumber(15))
