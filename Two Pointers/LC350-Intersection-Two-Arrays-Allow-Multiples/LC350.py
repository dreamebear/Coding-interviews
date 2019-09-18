class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        if not nums1 or not nums2:
            return []

        nums1.sort()
        nums2.sort()

        res = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return res


        # T:O(mlogm + nlogn)


"""
Follow up:

Q. What if the given array is already sorted? How would you optimize your algorithm?

If both arrays are sorted, I would use two pointers to iterate, which somehow resembles the merge process in merge sort.


Q. What if nums1's size is small compared to nums2's size? Which algorithm is better?

Suppose lengths of two arrays are N and M, the time complexity of my solution is O(N+M) and the space complexity if O(N) considering the hash. So it's better to use the smaller array to construct the counter hash.

Well, as we are calculating the intersection of two arrays, the order of array doesn't matter. We are totally free to swap to arrays.

Q. What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

Divide and conquer. Repeat the process frequently: Slice nums2 to fit into memory, process (calculate intersections), and write partial results to memory.

"""
