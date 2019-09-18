class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while (left + 1 < right):
            mid = left + (right - left) // 2

            if (nums[mid] == target):
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

        if (nums[left] == target):
            return left
        elif nums[right] == target:
            return right
        else:
            return -1



test = Solution()
nums = [-1,0,3,5,9,12]
target = 9
print(test.search(nums, target))