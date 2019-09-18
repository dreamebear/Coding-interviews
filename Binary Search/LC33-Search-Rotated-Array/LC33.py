class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # input / output type?
        # duplicate?
        # time / space requirement?

        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            elif nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid

        # print left
        # print right

        # exit condition: left + 1 == right
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1




test = Solution()
nums = [4,5,6,7,0,1,2]
target = 0

print(test.search(nums, target))