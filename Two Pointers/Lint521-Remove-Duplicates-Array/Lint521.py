"""
Given an array of integers, remove the duplicate numbers in it.

You should:
Do it in place in the array.
Move the unique numbers to the front of the array.
Return the total number of the unique numbers.

Notice
You don't need to keep the original order of the integers.

Example
Given nums = [1,3,1,4,4,2], you should:
Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
Return the number of unique integers in nums => 4.
Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.

Challenge
Do it in O(n) time complexity. Do it in O(nlogn) time without extra space.
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :param nums: List[int]
        :return: List[int]
        """

        if not nums:
            return 0

    # 1. count unique nums
        # seen = set()
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] not in seen:
        #         nums[count] = nums[i]
        #         seen.add(nums[i])
        #         count += 1
        # print(nums)
        # return count

    # T:O(n)  S:O(n)


    # 2. sort in place
    #     nums.sort()
    #     count = 1
    #     for i in range(1, len(nums)):
    #         # encounter with a new number
    #         if nums[i] != nums[i-1]:
    #             nums[i-1] = nums[i]
    #             count += 1
    #
    #     print(nums) # [1, 2, 3, 4, 4, 4]
    #     return count

    # T:O(nlogn) S:O(1)


        nums.sort()
        # i: unique number count
        # j: iteration index
        i , j = 0, 0
        while j < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
                if j >= len(nums):
                    print(nums) # [1, 2, 3, 4, 4, 4]
                    return i+1

            i += 1
            nums[i] = nums[j]

        print(nums)
        return i+1





test = Solution()
nums = [1,3,1,4,4,2]
print(test.removeDuplicates(nums))





