class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        if not A or len(A) < 2:
            return -1

            # return max < K
        A.sort()
        left, right = 0, len(A) - 1
        res = -1
        while left < right:
            if A[left] + A[right] < K:
                res = max(res, A[left] + A[right])
                left += 1
            else:
                right -= 1

        return res

        # T:O(n)  S:O(1)