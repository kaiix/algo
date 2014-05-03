package tree;

import java.util.ArrayList;

/*
 * http://oj.leetcode.com/problems/minimum-depth-of-binary-tree/
 */
public class MinDepth {
    public static class TreeNode {
        TreeNode left;
        TreeNode right;
        int val;
        TreeNode(int x) { val = x; }
    }

    public static int minDepth(TreeNode root) {
        // min-depth of a tree stops at the first leaf
        // when traverse in level order
        if (root != null) {
            ArrayList<TreeNode> siblings = new ArrayList<TreeNode>();
            siblings.add(root);
            int depth = 0;
            while (true) {
                final int count = siblings.size();
                if (count == 0) {
                    break;
                }
                depth++;
                for (int i = 0; i < count; i++) {
                    TreeNode node = siblings.get(0);
                    if (node.left != null) {
                        siblings.add(node.left);
                    }
                    if (node.right != null) {
                        siblings.add(node.right);
                    }
                    if (node.left == null && node.right == null) {
                        return depth;
                    }
                    siblings.remove(0);
                }
            }
        }
        return 0;
    }

    public static void main(String []args){
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        System.out.println(minDepth(root)); // 2

        /*
        root = new TreeNode(1);
        System.out.println(minDepth(root)); // 1

        root = new TreeNode(1);
        root.left = new TreeNode(2);
        System.out.println(minDepth(root)); // 2
        */
    }
}
