package list;

import java.util.ArrayList;

/*
 * http://oj.leetcode.com/problems/reorder-list/ 
 */

public class ReorderList {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public static void reorderList(ListNode head) {
        if (head != null && head.next != null) {
            ArrayList<ListNode> elems = new ArrayList<ListNode>();
            ListNode el = head;
            while (el != null) {
                elems.add(el);
                el = el.next;
            }
            
            ListNode p = null, q = null, tmp = null;
            for (int i = 0, j = elems.size()-1; i < j; i++, j--) {
                p = elems.get(i);
                q = elems.get(j);
                tmp = p.next;
                
                p.next = q;
                q.next = tmp;
                p = tmp;
            }
            if (p != null) {
                p.next = null;
            }
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

    public static void main(String []args){
        ListNode list;
        
        list = makeList(new int[] {1, 2, 3, 4});
        printList(list);
        reorderList(list);
        printList(list);

        list = makeList(new int[] {1});
        printList(list);
        reorderList(list);
        printList(list);

        list = makeList(new int[] {1, 2});
        printList(list);
        reorderList(list);
        printList(list);

        list = makeList(new int[] {1, 2, 3});
        printList(list);
        reorderList(list);
        printList(list);
        
        list = makeList(new int[] {1, 2, 3, 4, 5});
        printList(list);
        reorderList(list);
        printList(list);
    }
}
