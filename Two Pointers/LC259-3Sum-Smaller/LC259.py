class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums or len(nums) < 3:
            return 0

        nums.sort()

        count = 0
        for i in range(len(nums) - 2):
            # print i
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + nums[i] < target:
                    # print nums[i], nums[left], nums[right]
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count

        # T:O(n^2) S:O(1)