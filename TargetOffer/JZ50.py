#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return int整型
#
class Solution:
    def duplicate(self , numbers ):
        # write code here
        if not numbers:
            return -1
        res = {}
        l = len(numbers)
        for n in numbers:
            if n < 0 or n > l - 1:
                return -1
            if n not in res:
                res[n] = 1
            else:
                return n