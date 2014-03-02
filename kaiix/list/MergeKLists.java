package list;

import java.util.ArrayList;

/*
 * http://oj.leetcode.com/problems/merge-k-sorted-lists/
 */

public class MergeKLists {
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

    public static ListNode mergeKLists(ArrayList<ListNode> lists) {
        if (lists.size() == 0) {
            return null;
        }
        ListNode l1 = lists.get(0);
        lists.remove(0);
        return mergeTwoLists(l1, mergeKLists(lists));
    }
 
    public static void main(String []args){
        ArrayList<ListNode> lists = new ArrayList<ListNode>();
        lists.add(makeList(new int[] {1, 2, 3}));
        lists.add(makeList(new int[] {4, 5, 6}));
        lists.add(makeList(new int[] {7, 8, 9}));
        printList(mergeKLists(lists));

        lists = new ArrayList<ListNode>();
        lists.add(makeList(new int[] {1, 4, 9}));
        lists.add(makeList(new int[] {2, 3}));
        lists.add(makeList(new int[] {7, 10, 12}));
        printList(mergeKLists(lists));
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
