
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def findMid(self,head):
        if head is None:
            return head
        s=head
        f=head
        while f.next is not None and f.next.next is not None:
            f=f.next.next
            s=s.next
        return s.next

    def reverseList(self,head):
        if head is None or head.next is None:
            return head
        new_head=self.reverseList(head.next)

        head.next.next=head
        head.next=None
        return new_head

    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        
        mid=self.findMid(head)
        
        new_head=self.reverseList(mid)
        
        while new_head is not None:
            if head.val!=new_head.val:
                return False
            head=head.next
            new_head=new_head.next
        return True



        
