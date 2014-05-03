package tree;

import java.util.ArrayList;

/*
 * http://oj.leetcode.com/problems/binary-tree-level-order-traversal/
 */
public class BinaryTreeLevelOrderTraversal {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public static ArrayList<ArrayList<Integer>> levelOrder(TreeNode root) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if (root != null) {
            ArrayList<TreeNode> siblings = new ArrayList<TreeNode>();
            siblings.add(root);
            while (true) {
                final int count = siblings.size();
                if (count == 0) {
                    break;
                }
                ArrayList<Integer> siblingsValue = new ArrayList<Integer>();
                for (int i = 0; i < count; i++) {
                    TreeNode node = siblings.get(0);
                    siblingsValue.add(node.val);
                    if (node.left != null) siblings.add(node.left);
                    if (node.right != null) siblings.add(node.right);
                    siblings.remove(0);
                }
                result.add(siblingsValue);
            }

        }
        return result;
    }

    public static void main(String []args){
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        System.out.println(levelOrder(root));
    }
}
