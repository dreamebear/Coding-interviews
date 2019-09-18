# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 1:
            return False

        left, right = 1, n

        while (left + 1 < right):
            mid = left + (right - left) / 2

            # mid is bad version, first <= mid
            if isBadVersion(mid):
                right = mid
            else:
                # mid is not bad version, first > mid
                left = mid

        if isBadVersion(left):
            return left
        else:
            return right