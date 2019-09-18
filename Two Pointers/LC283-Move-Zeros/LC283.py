class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return []

        zero = 0
        # zero moves 1 step, nonzero moves until find nonzero number
        for nonzero in range(len(nums)):

            if nums[nonzero] == 0:
                continue

            # find nonzero number
            if nums[zero] == 0:
                nums[zero], nums[nonzero] = nums[nonzero], nums[zero]

            zero += 1



            # T:O(n)  S:O(1)
