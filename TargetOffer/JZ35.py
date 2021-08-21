# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.cnt = 0
    def InversePairs(self, data):
        # write code here

        def mergeSort(left, right):
            mid = int((left + right) / 2)
            if left < right:
                mergeSort(left, mid)
                mergeSort(mid + 1, right)
                merge(left, mid, right)


        def merge(left, mid, right):
            l = left
            r = mid + 1
            temp = []
            while l <= mid and r <= right:
                if data[l] <= data[r]:
                    temp.append(data[l])
                    l += 1
                else:
                    temp.append(data[r])
                    self.cnt += mid - l + 1
                    self.cnt %= 1000000007
                    r += 1
            while l <= mid:
                temp.append(data[l])
                l += 1
            while r <= right:
                temp.append(data[r])
                r += 1
            data[left: right + 1] = temp
        mergeSort(0, len(data) - 1)
        return self.cnt
