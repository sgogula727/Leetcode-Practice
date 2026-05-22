# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            s1 = list1.val 
            s2 = list2.val 

            if s1 > s2:
                current.next = ListNode(s2)
                current = current.next
                list2 = list2.next
            else:
                current.next = ListNode(s1)
                current = current.next
                list1 = list1.next

        if list1:
            current.next = list1
        else:
            current.next = list2
            

        return dummy.next
            