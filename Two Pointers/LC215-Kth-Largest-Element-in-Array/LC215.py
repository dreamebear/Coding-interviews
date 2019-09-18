class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if not nums or k < 1 or len(nums) < k:
            return None

        # if the array is sorted, then nums[len(nums)-k]
        # => N-k smallest
        return self.partition(nums, 0, len(nums) - 1, len(nums) - k)

    # return kth smallest element in nums[start, end+1]
    def partition(self, nums, start, end, k):
        # print start, end, k
        # we find the exact position of k
        if start == end:
            return nums[k]

        left, right = start, end
        # pivot = nums[end]
        pivot = nums[(start + end) // 2]
        # print pivot
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1

            # swap left & right
            if left <= right:
                # print left, right
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # print nums
        # print left, right
        # start ... right ... left ... end
        if left <= k:
            return self.partition(nums, left, end, k)

        if right >= k:
            return self.partition(nums, start, right, k)

        return nums[k]

        # T:O(n)  S:O(1)