# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # # 1. iterative
        if not head:
            return None

        pre, cur = None, head
        while cur:
            #print cur.val
            temp = cur.next

            cur.next = pre
            pre = cur
            cur = temp

        # exit when cur=None
        return pre

        # T:O(n)  S:O(1)

        # 2. recursive

        if not head or not head.next:
            return head

        # find last node
        newHead = self.reverseList(head.next)
        nextNode = head.next
        nextNode.next = head
        head.next = None

        return newHead

    # T: O(n). n is the list's length
    # S: O(n) The extra space comes from implicit stack space due to recursion. The recursion could go up to n levels deep.
