class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        # write your code here

        if not nums:
            return []

        if k >= len(nums):
            return [sum(nums)]

        left, right = 0, k
        cur = sum(nums[:k])
        res = [cur]

        while right < len(nums):
            cur = cur + nums[right] - nums[left]
            res.append(cur)
            right += 1
            left += 1

        return res

    # T:O(n)

test = Solution()
array = [1,2,7,8,5]
k = 3
print(test.winSum(array, k))