# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        if len(sequence) == 1:
            return True
        root = sequence[-1]
        x = len(sequence) - 1
        n = len(sequence)
        for i in range(len(sequence)):
            if sequence[i] > root:
                x = i
                break
        for i in range(x, len(sequence) - 1):
            if sequence[i] < root:
                return False
        if x == 0:
            return self.VerifySquenceOfBST(sequence[x:n - 1])
        elif x == n - 1:
            return self.VerifySquenceOfBST(sequence[:x])
        else:
            return self.VerifySquenceOfBST(sequence[:x]) and self.VerifySquenceOfBST(sequence[x:n - 1])
s = Solution()
print(s.VerifySquenceOfBST([4,5,6,7]))