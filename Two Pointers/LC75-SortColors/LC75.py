# one pass solution
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # one-pass: three pointers: left, index, right
        """
        设立三根指针，left, index, right。定义如下规则：
            left 的左侧都是 0（不含 left）
            right 的右侧都是 2（不含 right）
            index: unknown elements
        iterate index in nums:
            == 0: swap(left, index)
            == 2: swap(index, right)
            == 1: continue
        """
        # left <= index <= right

        left, index, right = 0, 0, len(nums) - 1
        while index <= right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                # left is in correct place, check further
                left += 1
                index += 1
                # move index because after swap, left has been checked
            elif nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                # right is in correct place
                right -= 1
                # after swap, index(the original right) has not checked yet
            else:
                index += 1


                # one pass: T:O(n) S:O(1)

# two pass solution using quicksort
class Solution(object):
    def quicksort(self, nums, start, flag):
        end = len(nums) - 1
        while start <= end:
            # should be on left
            while start <= end and nums[start] == flag:
                start += 1
            # should be on right
            while start <= end and nums[end] != flag:
                end -= 1

            if start <= end:
                # swap
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return start

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # two-pass: quicksort
        # 1. put 0 in the left
        # 2. put 1 in the left

        # find the index where all 0 on the left of index: search in [0, len(nums)-1]
        index0shouldbe = self.quicksort(nums, 0, 0)
        # print index0shouldbe
        # print nums
        # search in range [index0shouldbe, len(nums)-1]
        self.quicksort(nums, index0shouldbe, 1)

        # T:O(2n)  S:O(1)


