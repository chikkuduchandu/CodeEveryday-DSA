
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
    public ListNode findMid(ListNode head){
        if(head==null){
            return head;
        }
        ListNode s=head;
        ListNode f=head;
        while(f.next!=null && f.next.next!=null){
            f=f.next.next;
            s=s.next;
        }
        return s.next;
    }
    public ListNode reverseList(ListNode head){
        if(head==null || head.next== null){
            return head;
        }
        ListNode new_head=reverseList(head.next);
        head.next.next=head;
        head.next=null;
        return new_head;
    }
    public boolean isPalindrome(ListNode head) {
        ListNode mid=findMid(head);

        ListNode new_head=reverseList(mid);

        while(new_head!=null){
            if(head.val!=new_head.val){
                return false;
            }
            head=head.next;
            new_head=new_head.next;
        }
        return true;
    }
}
