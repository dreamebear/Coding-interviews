class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums or len(nums) < 3:
            return 0

        nums.sort()
        res = 0
        for i in range(2, len(nums)):
            if nums[i] == 0:
                continue

            left, right = 0, i - 1
            while left < right:
                # print i, left, right
                if nums[left] + nums[right] > nums[i]:

                    res += right - left
                    right -= 1
                else:
                    left += 1

        return res

        # T:O(n^2)  S:O(1)

    """
    前边做过两种题目
1， 两个数相加 == 某个数
2， 两个数相加 > 某个数

一般来讲这两类问题都是先排序，然后双指针一左，一右往中间走。

Triangle这题，需要根据上边两个情况找到匹配的情况带入，我刚开始第一遍就是先把第一个最小的边定好，然后在最小的右边用双指针
指中间和最大的边，发现这样并不能很好的解决问题，因为我最先定好的最小的值，后边的中间值和最大值不能带入到以上两种情况(1, 2)里边去，

后来想了一下，为了带入以上两种情况的第2种情况，我觉得应该先定最大值，然后再用双指针找最小值和中间值，这样就容易找到了
    """