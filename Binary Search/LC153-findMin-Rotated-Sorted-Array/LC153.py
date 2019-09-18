class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # input / output type?
        # time / space req
        # duplicate?
        # corner case?

        if not nums:
            return -1

        # not rotate
        if nums[-1] > nums[0]:
            return nums[0]

        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[-1]:
                left = mid
            else:
                right = mid
        # print left
        # print right

        return nums[left] if nums[left] < nums[right] else nums[right]




test = Solution()
nums = [3,4,5,1,2]
print(test.findMin(nums))
