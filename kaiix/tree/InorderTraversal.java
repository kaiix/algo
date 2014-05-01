package tree;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Stack;
import java.util.concurrent.TimeUnit;

/*
 * http://oj.leetcode.com/problems/binary-tree-inorder-traversal/
 */
public class InorderTraversal {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public static ArrayList<Integer> inorderTraversalRecursion(TreeNode root) {
        if (root == null) {
            return new ArrayList<Integer>();
        } else {
            ArrayList<Integer> result = new ArrayList<Integer>();
            result.addAll(inorderTraversalRecursion(root.left));
            result.add(root.val);
            result.addAll(inorderTraversalRecursion(root.right));
            return result;
        }
    }

    public static void inorderTraversalTailRecursion(TreeNode root, ArrayList<Integer> result) {
        if (root != null) {
            inorderTraversalTailRecursion(root.left, result);
            result.add(root.val);
            inorderTraversalTailRecursion(root.right, result);
        }
    }

    public static ArrayList<Integer> inorderTraversalIteration(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<Integer>();

        if (root == null) {
            return result;
        }

        Stack<TreeNode> path = new Stack<TreeNode>();
        HashSet<TreeNode> visitedNodes = new HashSet<TreeNode>();

        TreeNode node = root;
        while (true) {
            if (node.left != null && !visitedNodes.contains(node.left)) {
                path.push(node);
                node = node.left;
            } else {
                if (!visitedNodes.contains(node)) {
                    visitedNodes.add(node);
                    result.add(node.val);
                }

                if (node.right != null && !visitedNodes.contains(node.right)) {
                    path.push(node);
                    node = node.right;
                } else {
                    if (!path.isEmpty()) {
                        node = path.pop();
                    } else {
                        break;
                    }
                }
            }
        }
        return result;
    }

    public static void main(String []args){
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(3);
        root.left.right = new TreeNode(4);
        root.right = new TreeNode(5);
        root.right.left = new TreeNode(6);

        long start;
        ArrayList<Integer> result;

        start = System.nanoTime();
        result = inorderTraversalRecursion(root);
        System.out.println("recursion method cost " + TimeUnit.NANOSECONDS.toMillis(System.nanoTime()-start) + " ms");
        System.out.println(result);

        result = new ArrayList<Integer>();
        start = System.nanoTime();
        inorderTraversalTailRecursion(root, result);
        System.out.println("tail-recursion method cost " + TimeUnit.NANOSECONDS.toMillis(System.nanoTime()-start) + " ms");
        System.out.println(result);

        start = System.nanoTime();
        result = inorderTraversalIteration(root);
        System.out.println("iteration method cost " + TimeUnit.NANOSECONDS.toMillis(System.nanoTime()-start) + " ms");
        System.out.println(result);
    }
}
