/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteMiddle(ListNode head) {
        ListNode dummy=new ListNode(0,head);
        ListNode s=dummy;
        ListNode f=head;
        int count=0;
        while(f!=null){
            f=f.next;
            count+=1;
            if(count%2==0){
                s=s.next;
            }
        }
        s.next=s.next.next;
        return dummy.next;

    }
}
