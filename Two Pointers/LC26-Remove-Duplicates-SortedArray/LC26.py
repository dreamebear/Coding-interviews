class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        # len(nums) > 1
        count = 1
        for i in range(1, len(nums)):
            # have unique number
            if nums[i] != nums[i - 1]:
                nums[count] = nums[i]
                count += 1

        # print nums
        return count

        # T:O(n)  S:O(1)