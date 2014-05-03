package tree;

/*
 * http://oj.leetcode.com/problems/balanced-binary-tree/
 */
public class BalancedBinaryTree {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public static boolean isBalanced(TreeNode root) {
        if (root != null) {
            if (Math.abs(heightOfTree(root.left) - heightOfTree(root.right)) <= 1) {
                return isBalanced(root.left) && isBalanced(root.right);
            } else {
                return false;
            }
        } else {
            return true;
        }
    }

    private static int heightOfTree(TreeNode node) {
        if (node == null) {
            return 0;
        } else {
            return 1 + Math.max(heightOfTree(node.left), heightOfTree(node.right));
        }
    }

    public static void main(String []args){
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(3);
        root.left.left.left = new TreeNode(4);
        root.right = new TreeNode(2);
        root.right.right = new TreeNode(3);

        System.out.println("balanced = " + isBalanced(root));
    }
}
