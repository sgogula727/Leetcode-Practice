# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        holder = ListNode(0)
        current = holder

        while l1 or l2 or carry:
            s1 = l1.val if l1 is not None else 0
            s2 = l2.val if l2 is not None else 0
            sum = s1+s2+carry

            carry = sum // 10
            digit = sum % 10

            current.next= ListNode(digit)
            current = current.next
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return holder.next