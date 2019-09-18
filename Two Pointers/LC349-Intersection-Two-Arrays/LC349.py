class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        if not nums1 or not nums2:
            return []

            # sol 1. hash set

        #         seen = set()
        #         for num in nums1:
        #             if num not in seen:
        #                 seen.add(num)

        #         res = []
        #         for num in nums2:
        #             if num in seen:
        #                 res.append(num)
        #                 seen.remove(num)

        #         return res

        # T:O(m+n)  S:O(m, n)

        # sol2: sort + two pointer

        nums1.sort()
        nums2.sort()

        i = j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not res or nums1[i] != res[-1]:
                    res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return res
        # T:O(mlogm + nlogn) S:O(1)


test = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(test.intersection(nums1, nums2))
