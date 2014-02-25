package list;

/*
 * http://oj.leetcode.com/problems/rotate-list/
 */

public class RotateRight {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public static ListNode rotateRight(ListNode head, int n) {
        if (head != null && head.next != null) {
            ListNode p, q;
            int size = 0;
            
            p = head;
            while (p != null) {
                size++;
                p = p.next;
            }
            n = n % size;
            
            p = head;
            q = head;
            for (int i = 0; i < n; i++) {
                q = q.next;
            }
            if (q == null) return head;
            while (q.next != null) {
                p = p.next;
                q = q.next;
            }
            q.next = head;
            head = p.next;
            p.next = null;
        }
        return head;
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
        ListNode list;
        
        list = makeList(new int[] {1, 2, 3, 4, 5});
        printList(list);
        list = rotateRight(list, 2);
        printList(list);

        list = makeList(new int[] {1});
        printList(list);
        list = rotateRight(list, 1);
        printList(list);

        list = makeList(new int[] {1, 2});
        printList(list);
        list = rotateRight(list, 3);
        printList(list);
    }
}
