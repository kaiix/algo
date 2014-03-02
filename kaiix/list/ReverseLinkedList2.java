package list;

/*
* http://oj.leetcode.com/problems/reverse-linked-list-ii/
*/

public class ReverseLinkedList2 {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public static ListNode reverseBetween(ListNode head, int m, int n) {
        if (head != null && head.next != null) {
            if (m == 1) {
                ListNode p = null;
                ListNode q = head;
                for (int i = 0; i < n; i++) {
                    ListNode tmp = q.next;
                    q.next = p;
                    p = q;
                    q = tmp;
                }
                if (q != null) {
                    head.next = q;
                }
                return p;
            } else {
                ListNode s = head;
                ListNode p = s.next;
                ListNode q = p.next;
                for (int i = 0; i < n-2; i++) {
                    if (i < m-2) {
                        s = s.next;
                        p = p.next;
                        q = q.next;
                    } else {
                        ListNode tmp = q.next;
                        q.next = p;
                        p = q;
                        q = tmp;
                    }
                }
                ListNode tmp = s.next;
                s.next = p;
                tmp.next = q;
                return head;
            }
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
        
        list = makeList(new int[] {1, 2});
        printList(list);
        list = reverseBetween(list, 1, 2);
        printList(list);
        
        list = makeList(new int[] {1, 2, 3});
        printList(list);
        list = reverseBetween(list, 1, 3);
        printList(list);
        
        list = makeList(new int[] {1, 2, 3});
        printList(list);
        list = reverseBetween(list, 1, 2);
        printList(list);
        
        list = makeList(new int[] {1, 2, 3, 4, 5});
        printList(list);
        list = reverseBetween(list, 1, 3);
        printList(list);
        
        list = makeList(new int[] {1, 2, 3, 4, 5});
        printList(list);
        list = reverseBetween(list, 2, 4);
        printList(list);

        list = makeList(new int[] {1, 2, 3, 4, 5});
        printList(list);
        list = reverseBetween(list, 1, 4);
        printList(list);
        
        list = makeList(new int[] {1, 2, 3, 4, 5});
        printList(list);
        list = reverseBetween(list, 2, 5);
        printList(list);

        list = makeList(new int[] {1, 2, 3, 4, 5});
        printList(list);
        list = reverseBetween(list, 3, 5);
        printList(list);
    }
}
