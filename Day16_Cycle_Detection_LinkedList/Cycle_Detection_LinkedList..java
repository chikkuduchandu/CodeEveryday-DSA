/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if(head==null){
            return null;
        }
        ListNode s=head;
        ListNode f=head;

        while(f.next!=null && f.next.next!=null){
            s=s.next;
            f=f.next.next;
            if(s==f){
                s=head;
                while(s!=f){
                    s=s.next;
                    f=f.next;
                }
                return s;
            }
        }
        return null;
    }
}
