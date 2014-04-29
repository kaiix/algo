package tree;

/*
 * http://oj.leetcode.com/problems/same-tree/
 */
public class SameTree {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        public TreeNode(int x) { val = x; }
    }

    public static boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        } else if (p != null && q != null) {
            if (p.val == q.val) {
                return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(isSameTree(null, null));

        TreeNode p = new TreeNode(0);
        TreeNode q = new TreeNode(0);
        System.out.println(isSameTree(p, q));

        q.val = 1;
        System.out.println(isSameTree(p, q));

        q = null;
        System.out.println(isSameTree(p, q));

        p.left = new TreeNode(1);
        p.left.right = new TreeNode(2);
        q = new TreeNode(0);
        q.left = new TreeNode(1);
        q.left.right = new TreeNode(2);
        System.out.println(isSameTree(p, q));
    }
}
