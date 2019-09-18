# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return None

        # 1. check if has cycle
        slow, fast = head, head.next
        while slow != fast:
            # will return False if not have cycle
            if fast == None or fast.next == None:
                return None

            slow = slow.next
            fast = fast.next.next

        # slow and fast meet
        # 2. find the start node
        slow = slow.next
        while head != slow:
            slow, head = slow.next, head.next

        return slow


        # T:O(n) S:O(1)