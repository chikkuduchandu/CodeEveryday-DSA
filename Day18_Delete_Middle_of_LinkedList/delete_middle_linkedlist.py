# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode()
        dummy.next=head
        s=dummy
        f=head
        count=0
        while f is not None:
            f=f.next
            print(s.val)
            count+=1
            if(count%2==0):
                s=s.next
        s.next=s.next.next
        return dummy.next
        
