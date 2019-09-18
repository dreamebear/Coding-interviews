class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        if not arr or k == 0:
            return []

        if k >= len(arr):
            return arr

        # 1. find the index of the element closest to x: binary search
        index = -1
        left, right = 0, len(arr) - 1

        # if we can find element exactly equals to x, find its index
        while left + 1 < right:
            mid = left + (right - left) // 2

            if arr[mid] == x:
                index = mid
                break
            elif arr[mid] < x:
                left = mid
            else:
                right = mid

        # if we cannot find element equals to x, find the one closest to it
        if index == -1:
            if x - arr[left] <= arr[right] - x:
                index = left
            else:
                index = right

        # print index
        # 2. expand to k length: two pointer
        count = 1
        start = end = index

        while (count < k):
            if start == 0:
                end += 1
            elif end == len(arr) - 1:
                start -= 1
            else:

                if (x - arr[start - 1]) <= (arr[end + 1] - x):
                    start -= 1
                else:
                    end += 1

            count += 1

        return arr[start:end + 1]


test = Solution()
arr = [1,2,3,4,5]
k=4
x=-1
print(test.findClosestElements(arr, k, x))