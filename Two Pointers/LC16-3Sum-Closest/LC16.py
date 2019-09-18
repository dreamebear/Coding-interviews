class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # how many pairs? tie?

        # if not nums or len(nums) < 3:
        #     return

        nums.sort()

        res = float('inf')
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                cursum = nums[left] + nums[right] + nums[i]

                if abs(cursum - target) < abs(res - target):
                    res = cursum

                if cursum < target:
                    left += 1

                elif cursum > target:
                    right -= 1


                else:
                    return cursum

        return res

        # T:O(n^2)  S:O(1)