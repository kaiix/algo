package list;

/*
 * http://oj.leetcode.com/problems/merge-two-sorted-lists/
 */

public class MergeTwoLists {

    public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                l1.next = mergeTwoLists(l1.next, l2);
                return l1;
            } else {
                l2.next = mergeTwoLists(l1, l2.next);
                return l2;
            }
        } else if (l1 == null) {
            return l2;
        } else {
            return l1;
        }
    }
 
    public static void main(String []args){
        ListNode list;
        
        list = mergeTwoLists(
                makeList(new int[] {1, 3, 5}),
                makeList(new int[] {2, 4, 6})
                );
        printList(list);
        
        list = mergeTwoLists(
                makeList(new int[] {2, 4, 6}),
                makeList(new int[] {1, 3, 5})
                );
        printList(list);
        
        list = mergeTwoLists(
                makeList(new int[] {1, 3, 5}),
                null
                );
        printList(list);
        
        list = mergeTwoLists(
                null,
                makeList(new int[] {2, 4, 6})
                );
        printList(list);
        
        list = mergeTwoLists(
                null,
                null
                );
        printList(list);
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
