#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @return bool布尔型
#
class Solution:
    def isNumeric(self , str ):
        # write code here
        def is_int(s):
            if s ==  "":
                return False
            if '.' in s:
                return False
            if s[0] == '+' or s[0] == '-':
                if len(s) == 1:
                    return False
                else:
                    for ss in s[1:]:
                        if ss > '9' or ss == '+' or ss == '-':
                            return False
                    return True
            for ss in s:
                if ss > '9' or ss == '+' or ss == '-':
                    return False
            return True
        def is_float(s):
            if s == "":
                return False
            if '.' not in s:
                return False
            part = s.split('.')
            if len(part) > 2:
                return False
            if part[0] == "" and part[1] == "":
                return False
            if len(part[0]) and (part[0][0] == '+' or part[0][0] == '-'):
                if len(part[0]) == 1 and (part[0] == '+' or part[0] == '-') and part[1] == "":
                    return False
                # else:
                for ss in part[0][1:]:
                    if ss > '9' or ss == '+' or ss == '-':
                        return False
                for ss in part[1]:
                    if ss > '9' or ss == '+' or ss == '-':
                        return False
                return True
            for ss in part[0]:
                if ss > '9' or ss == '+' or ss == '-':
                    return False
            for ss in part[1]:
                if ss > '9' or ss == '+' or ss == '-':
                    return False
            return True
        str = str.strip()
        if 'e' in str or 'E' in str:
            if 'e' in str:
                part = str.split('e')
            else:
                part = str.split('E')
            if len(part) > 2:
                return False
            return (is_float(part[0]) or is_int(part[0])) and is_int(part[1])

        if '.' in str:
            return is_float(str)
        return is_int(str)

s = Solution()
print(s.isNumeric("92e1740e91"))