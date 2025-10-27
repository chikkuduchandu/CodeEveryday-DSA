# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        fast=head
        count=0
        while fast is not None :
            fast=fast.next
            count+=1
            if count==n:
                break
        if fast is None:
            return head.next
        slow=head
        while fast.next is not None:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head

            
