class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # how many pairs do we need to find? any or all?
        # do we have duplicates in numbers? how to deal with such situation?
        # what if not find?


        if not numbers or len(numbers) < 2:
            return []

        # when array is in sorted order, use two pointers
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                # result index is starts from 1
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                # need to find larger
                left += 1
            else:
                right -= 1

        return []
