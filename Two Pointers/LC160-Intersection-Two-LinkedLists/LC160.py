# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        # cycle in linkedlist?

        # sol1. iteration until two pointers meet
        """
        if headA == None or headB == None:
            return None

        pointerA, pointerB = headA, headB

        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

#             if use: 
#             pointerA = pointerA.next if pointerA else headB
#             cause TLE when two linkedlists have no intersection

        # exit: when pointerA == pointerB
        return pointerA

    # T:O(m + n) S:O(1)
        """

        # sol2: count the length of two linked lists first

        if headA == None or headB == None:
            return None

        lengthA, lengthB = self.getLength(headA), self.getLength(headB)

        diff = abs(lengthA - lengthB)
        if lengthA > lengthB:
            longer = headA
            shorter = headB
        else:
            longer = headB
            shorter = headA

        while diff > 0:
            longer = longer.next
            diff -= 1

        while longer != shorter:
            longer = longer.next
            shorter = shorter.next

            # exit: when longer == shorter, can be both equal None
        return longer

    def getLength(self, head):
        count = 0
        while head:
            count += 1
            head = head.next

        return count

        # T:O(m+n) S:O(1)


test = Solution()