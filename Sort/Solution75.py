class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_ptr, two_ptr = 0, len(nums) - 1
        i = 0
        while i <= two_ptr:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                nums[i], nums[zero_ptr] = nums[zero_ptr], nums[i]
                zero_ptr += 1
                i += 1
            else:
                nums[i], nums[two_ptr] = nums[two_ptr], nums[i]
                two_ptr -= 1