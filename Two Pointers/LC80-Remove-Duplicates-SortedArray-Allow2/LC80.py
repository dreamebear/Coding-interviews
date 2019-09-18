class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        # current count of unique numbers
        count = 0
        for num in nums:
            # start with the first 2, or find a new distinct number
            if count < 2 or num > nums[count - 2]:
                nums[count] = num
                count += 1

        return count

        # T:O(n)  S:O(1)


# if we allow duplicates appeared at most k times

# def removeDuplicatesK(self, nums):

#         count = 0
#         for num in nums:
#             if count < k or num > nums[count-k]:
#                 nums[count] = num
#                 count += 1

#         return count


