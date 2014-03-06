package list;


/*
 * http://oj.leetcode.com/problems/partition-list/
 */

public class PartitionList {
    public static ListNode partition(ListNode head, int x) {
        if (head != null && head.next != null) {
            ListNode p = head, lh = null, gh = null;
            while (p != null) {
                if (p.val < x) {
                    if (p == head) {
                        lh = p;
                        p = p.next;
                    } else {
                        if (lh == null) {
                            ListNode tmp = p.next;
                            gh.next = tmp;
                            p.next = head;
                            head = p;
                            p = tmp;
                            lh = head;
                        } else if (lh.next == p) {
                            lh = p;
                            p = p.next;
                        } else {
                            ListNode tmp = p.next;
                            gh.next = tmp;
                            p.next = lh.next;
                            lh.next = p;
                            lh = p;
                            p = tmp;
                        }
                    }
                } else {
                    gh = p;
                    p = p.next;
                }
            }
        }
        return head;
    }
 
    public static void main(String []args){
        ListNode list;
        list = makeList(new int[] {1, 4, 3, 2, 5, 2});
        printList(partition(list, 3));

        list = makeList(new int[] {4, 1, 3, 2, 5, 2});
        printList(partition(list, 3));
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
