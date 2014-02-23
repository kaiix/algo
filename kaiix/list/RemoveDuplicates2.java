package list;

import java.util.HashSet;

/*
 * http://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
 */

public class RemoveDuplicates2 {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public static ListNode deleteDuplicates(ListNode head) {
        HashSet<Integer> valsToRemove = new HashSet<Integer>();
        
        ListNode p = head;
        while (p != null && p.next != null) {
            if ((p.val == p.next.val) && !valsToRemove.contains(p.val)) {
                valsToRemove.add(p.val);
            } else {
                p = p.next;
            }
        }
        
        p = head;
        ListNode prev = p;
        while (p != null) {
            if (valsToRemove.contains(p.val)) {
                if (p == head) {
                    head = p.next;
                } else {
                    prev.next = p.next;
                }
            } else {
                prev = p;
            }
            p = p.next;
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
        ListNode list = makeList(new int[] {1, 2, 3, 3, 4, 4, 5});
        printList(list);
        
        deleteDuplicates(list);
        printList(list);

        list = makeList(new int[] {1, 1});
        printList(list);
        deleteDuplicates(list);
        printList(list);
    }
}
