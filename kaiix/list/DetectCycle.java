package list;

import java.util.HashSet;


/*
 * http://oj.leetcode.com/problems/linked-list-cycle-ii/
 */

public class DetectCycle {

    /*
     * 1->2->3
     *    |<-|
     * returns 2
     */
    public static ListNode detectCycle(ListNode head) {
        HashSet<ListNode> visitedNodes = new HashSet<ListNode>();
        ListNode p = head;
        while (p != null && !visitedNodes.contains(p)) {
            visitedNodes.add(p);
            p = p.next;
        }
        return p;
    }

    public static void main(String []args){
        ListNode list = new ListNode(1);
        list.next = new ListNode(2);
        list.next.next = new ListNode(3);
        list.next.next.next = list.next;
        System.out.println("cycle start at " + detectCycle(list).val);
    }

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
    }
}
