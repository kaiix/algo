package tree;

/*
 * http://oj.leetcode.com/problems/symmetric-tree/
 */
public class SymmetricTree {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public static boolean isSymmetric(TreeNode root) {
        if (root != null) {
            return isMirror(root.left, root.right);
        } else {
            return true;
        }
    }

    private static boolean isMirror(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        } else if (p != null && q != null && p.val == q.val) {
            return isMirror(p.left, q.right) && isMirror(p.right, q.left);
        } else {
            return false;
        }
    }

    public static void main(String []args){
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(3);
        root.right = new TreeNode(2);
        root.right.right = new TreeNode(3);

        System.out.println("symmetric tree = " + isSymmetric(root));
    }
}
