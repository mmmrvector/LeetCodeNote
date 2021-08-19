class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def countAlphabet(s):
            res = {}
            for a in s:
                if a not in res:
                    res[a] = 1
                else:
                    res[a] += 1
            ret = ""
            key_list = []
            for key in res:
                key_list.append(key)
            key_list.sort()
            for key in key_list:
                ret += key * res[key]
            return ret
        ret = {}
        for word in strs:
            res = countAlphabet(word)
            if res not in ret:
                ret[res] = [word]
            else:
                ret[res].append(word)
        res = []
        for key in ret:
            res.append(ret[key])

        return res


s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))