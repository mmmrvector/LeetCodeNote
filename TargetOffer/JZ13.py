#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    def reOrderArray(self , array ):
        # write code here
        odd = []
        even = []
        for a in array:
            if a % 2 == 0:
                even.append(a)
            else:
                odd.append(a)
        return odd + even