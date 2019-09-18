class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # empty array or len(nums) < 2
        if not nums or len(nums) < 2:
            return [-1, -1]

        # hmap = {val: index}
        hmap = {}

        for index, val in enumerate(nums):
            diff = target - val

            if diff in hmap:
                return [hmap[diff], index]

            hmap[val] = index

            # time: O(n)
            # space: O(n)


test = Solution()
nums = [2, 7, 11, 15]
target = 9
print(test.twoSum(nums, target))