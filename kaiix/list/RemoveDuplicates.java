package list;

/*
 * http://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/
 */

public class RemoveDuplicates {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public static ListNode deleteDuplicates(ListNode head) {
        ListNode p = head;
        while (p != null && p.next != null) {
            if (p.val == p.next.val) {
                p.next = p.next.next;
            } else {
                p = p.next;
            }
        }
        return head;
    }
    
    private static ListNode makeList(int[] elems) {
        // make sentinel
        ListNode head = new ListNode(-1);
        head.next = null;
        
        ListNode prev = head;
        
        for (int i : elems) {
            ListNode node = new ListNode(i);
            prev.next = node;
            node.next = null;
            prev = node;
        }
        
        return head;
    }
    
    private static void printList(ListNode head) {
        head = head.next; // jump sentinel
        while (head != null) {
            System.out.print(head.val + "->");
            head = head.next;
        }
        System.out.println("null");
    }

    public static void main(String []args){
        ListNode list = makeList(new int[] {1, 1, 2, 3, 3});
        printList(list);
        
        deleteDuplicates(list);
        printList(list);
    }
}
