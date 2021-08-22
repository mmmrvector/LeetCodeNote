# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        numbers = sorted(numbers)
        zeros = 0
        for a in numbers:
            if a == 0:
                zeros += 1
        inter = [0]
        for i in range(zeros, 4):
            inter.append(numbers[i + 1] - numbers[i])
        if sum(inter) - (4 - zeros) <= zeros and sum(inter) - (4 - zeros) >= 0:
            return True
        return False