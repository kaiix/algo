package tree;

import java.util.ArrayList;
import java.util.Stack;

/*
 * http://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/
 */
public class FlattenBinaryTree {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public static void flatten(TreeNode root) {
        ArrayList<TreeNode> visitedNodes = new ArrayList<TreeNode>();

        if (root == null) {
            return;
        }

        Stack<TreeNode> path = new Stack<TreeNode>();

        TreeNode sentinel = new TreeNode(-1);
        sentinel.left = root;

        visitedNodes.add(sentinel);
        TreeNode node = root;
        while (true) {
            if (!visitedNodes.contains(node)) {
                visitedNodes.add(node);
            }
            if (node.left != null && !visitedNodes.contains(node.left)) {
                path.push(node);
                node = node.left;
            } else if (node.right != null && !visitedNodes.contains(node.right)) {
                path.push(node);
                node = node.right;
            } else {
                if (path.isEmpty()) {
                    break;
                }
                node = path.pop();
            }
        }

        while (true) {
            node = visitedNodes.get(0);
            visitedNodes.remove(0);
            if (visitedNodes.isEmpty()) {
                node.left = null;
                node.right = null;
                break;
            } else {
                node.left = null;
                node.right = visitedNodes.get(0);
            }
        }
    }

    public static void main(String []args){
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(3);
        root.left.right = new TreeNode(4);
        root.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);

        flatten(root);
        printTree(root);
    }

    private static void printTree(TreeNode root) {
        if (root == null) {
            System.out.print("#");
        } else {
            System.out.print(root.val);
            System.out.print("->l");
            printTree(root.left);
            System.out.print("->r");
            printTree(root.right);
        }
    }
}
