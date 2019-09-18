import heapq


class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """

        # heapify: linear time, in place
        heapq.heapify(nums)

        # maintain a max heap with length=k
        self.heap = nums
        # print self.heap
        while len(self.heap) > k:
            heapq.heappop(self.heap)

        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # because heapq is a min-heap, the top one is always the k largest element: heap[0] is the k largest

        # if len(heap) < k: insert
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)

        else:
            # else: replace if val > heap[0]
            if val > self.heap[0]:
                heapq.heapreplace(self.heap, val)

        return self.heap[0]

        # add T:O(logn)  S:O(n)



        # Your KthLargest object will be instantiated and called as such:
        # obj = KthLargest(k, nums)
        # param_1 = obj.add(val)