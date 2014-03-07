package list;


/*
 * http://oj.leetcode.com/problems/insertion-sort-list/
 */

public class InsertionSortList {
    public static ListNode insertionSortList(ListNode head) {
        if (head != null && head.next != null) {
            ListNode sortedTail = head;
            while (sortedTail.next != null) {
                ListNode current = sortedTail.next;
                if (current.val >= sortedTail.val) {
                    sortedTail = current;
                } else {
                    sortedTail.next = current.next;
                    ListNode p = null, q = head;
                    while (q != sortedTail.next && current.val > q.val) {
                        p = q;
                        q = q.next;
                    }
                    if (p == null) {
                        head = current;
                    } else {
                        p.next = current;
                    }
                    current.next = q;
                }
            }
        }
        
        return head;
    }

    public static void main(String []args){
        printList(insertionSortList(makeList(new int[] {2, 1})));
        printList(insertionSortList(makeList(new int[] {1, 3, 2})));
        printList(insertionSortList(makeList(new int[] {5, 4, 3, 1, 2})));
        printList(insertionSortList(makeList(new int[] {5, 3, 1})));
        printList(insertionSortList(makeList(new int[] {4, 3, 2, 1, 0})));
        printList(insertionSortList(makeList(new int[] {3, 2, 4})));
    }   
    
    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
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
}
