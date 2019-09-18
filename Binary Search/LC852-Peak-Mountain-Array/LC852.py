class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # input / output
        # how many peak?
        # len(A) >= 3

        if not A:
            return -1

        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2

            if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid

            elif A[mid - 1] < A[mid] < A[mid + 1]:
                left = mid
            else:
                right = mid


test = Solution()
A = [0,2,1,0]
print(test.peakIndexInMountainArray(A))