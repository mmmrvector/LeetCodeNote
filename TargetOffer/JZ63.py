# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.arr = []
    def Insert(self, num):
        # write code here
        if len(self.arr) == 0:
            self.arr = [num]
        else:
            for i in range(len(self.arr)):
                if self.arr[i] >= num:
                    self.arr.insert(i, num)
                    return
            self.arr.append(num)
    def GetMedian(self):
        # write code here
        if len(self.arr) %2 == 1:
            return self.arr[int(len(self.arr) / 2)]
        else:
            return (self.arr[int(len(self.arr) / 2)] + self.arr[int(len(self.arr)/ 2) - 1]) / 2