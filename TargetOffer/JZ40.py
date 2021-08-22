#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    def FindNumsAppearOnce(self , array ):
        # write code here
        x = 0
        for a in array:
            x ^= a
        mask = 1
        while x & mask == 0:
            mask = mask << 1
        a = 0
        b = 0

        for n in array:
            if n & mask == 0:
                a ^= n
            else:
                b ^= n
        if a < b:
            return [a, b]
        else:
            return [b, a]