# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        cur = head
        count = 0

        while cur and count < k:
            cur = cur.next
            count += 1

        if count == k:
            cur = self.reverseKGroup(cur, k)
            # print cur.val
            while count > 0:
                """
                k = 3
                1   -> 2 -> 3 -> 4 -> 5
                head  temp       cur

                """
                temp = head.next
                head.next = cur

                cur = head
                head = temp

                count -= 1

            head = cur

        return head

 # T:O(n)  S:O(n) - recursive stack space