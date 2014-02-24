package list;

/*
 * http://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/
 */

public class RemoveNthFromEnd {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public static ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode sentinel = new ListNode(-1);
        sentinel.next = head;
        ListNode prev = sentinel;
        ListNode tail = sentinel;
        for (int i = 0; i < n; i++) {
            tail = tail.next;
        }
        while (tail.next != null) {
            prev = prev.next;
            tail = tail.next;
        }
        prev.next = prev.next.next;
        return sentinel.next;
    }
    
    private static ListNode makeList(int[] elems) {
        ListNode head = new ListNode(-1);
        head.next = null;
        
        ListNode prev = head;
        
        for (int i : elems) {
            ListNode node = new ListNode(i);
            prev.next = node;
            node.next = null;
            prev = node;
        }
        
        return head.next;
    }
    
    private static void printList(ListNode head) {
        while (head != null) {
            System.out.print(head.val + "->");
            head = head.next;
        }
        System.out.println("null");
    }

    public static void main(String []args){
        ListNode list = makeList(new int[] {1, 2, 3, 4, 5});
        printList(list);
        removeNthFromEnd(list, 2);
        printList(list);

        System.out.println("********");
        
        list = makeList(new int[] {1});
        printList(list);
        list = removeNthFromEnd(list, 1);
        printList(list);
    }
}
