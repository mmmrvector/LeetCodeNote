class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dict ={}
        res = []
        for i in range(len(s) - 9):
            if s[i: i + 10] not in dict:
                dict[s[i:i+10]] = 1
            else:
                dict[s[i:i+10]] += 1
        for x in dict.keys():
            if dict[x] > 1:
                res.append(x)
        return res
s = Solution()
print(s.findRepeatedDnaSequences("AAAAAAAAAAA"))