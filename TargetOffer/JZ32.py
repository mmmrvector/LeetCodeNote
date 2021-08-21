# -*- coding:utf-8 -*-
class Solution:

    def PrintMinNumber(self, numbers):
        import functools
        # write code here
        def compare(a, b):
            if str(a) + str(b) > str(b) + str(a):
                return 1
            elif str(a) + str(b) < str(b) + str(a):
                return -1
            else:
                return 0
        return "".join(sorted([ str(x) for x in numbers], key=functools.cmp_to_key(compare)))