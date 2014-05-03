package tree;

import java.util.Arrays;

/*
 * http://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
 */
public class SortedArrayToBST {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public static TreeNode sortedArrayToBST(int[] num) {
        if (num.length > 0) {
            int mid = num.length % 2 == 0 ? num.length / 2 : (num.length + 1) / 2; mid -= 1;
            TreeNode root = new TreeNode(num[mid]);
            if (mid > 0) {
                root.left = sortedArrayToBST(Arrays.copyOfRange(num, 0, mid));
            }
            if (mid+1 < num.length) {
                root.right = sortedArrayToBST(Arrays.copyOfRange(num, mid + 1, num.length));
            }
            return root;
        } else {
            return null;
        }
    }

    private static void printTree(TreeNode root) {
        if (root == null) {
            System.out.print("#");
        } else {
            System.out.print(root.val);
            System.out.print(" ");
            printTree(root.left);
            System.out.print(" ");
            printTree(root.right);
        }
    }

    public static void main(String []args){
        printTree(sortedArrayToBST(new int[]{1}));
        System.out.println();
        printTree(sortedArrayToBST(new int[]{1, 2, 3, 4}));
    }
}
