package tree;

/*
 * http://oj.leetcode.com/problems/maximum-depth-of-binary-tree/
 */
public class MaxDepth {
    public static class TreeNode {
        TreeNode left;
        TreeNode right;
    }

    public static int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        } else if (root.left == null && root.right == null) {
            return 1;
        } else {
            return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
        }
    }

    public static void main(String []args){
        TreeNode root = new TreeNode();
        root.left = null;
        root.right = new TreeNode();
        root.right.left = null;
        root.right.right = null;
        System.out.println(maxDepth(root));

        root = new TreeNode();
        root.left = new TreeNode();
        root.right = new TreeNode();
        root.right.left = new TreeNode();
        root.right.right = new TreeNode();
        root.right.left.left = new TreeNode();
        System.out.println(maxDepth(root));

        root = new TreeNode();
        System.out.println(maxDepth(root));
    }
}
