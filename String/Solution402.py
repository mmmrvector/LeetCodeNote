class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)
        if n == 1:
            return "0"
        #rm = []
        i = 0
        while i < len(num) -1:
            if num[i] > num[i + 1]:
                num = num[:i] + num[i + 1:]
                k -= 1
                if k == 0:
                    break
                if i - 1 >= 0:
                    i = i - 1
            else:
                i += 1

        while k > 0:
            num = num[:-1]
            k -= 1
        if num == "":
            return "0"
        return str(int(num))
s = Solution()
print(s.removeKdigits("10001", 4))