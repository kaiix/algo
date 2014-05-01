package tree;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Stack;
import java.util.concurrent.TimeUnit;

/*
 * http://oj.leetcode.com/problems/binary-tree-preorder-traversal/
 */
public class PreorderTraversal {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public static ArrayList<Integer> preorderTraversalRecursion(TreeNode root) {
        if (root == null) {
            return new ArrayList<Integer>();
        } else {
            ArrayList<Integer> result = new ArrayList<Integer>();
            result.add(root.val);
            result.addAll(preorderTraversalRecursion(root.left));
            result.addAll(preorderTraversalRecursion(root.right));
            return result;
        }
    }

    public static void preorderTraversalTailRecursion(TreeNode root, ArrayList<Integer> result) {
        if (root != null) {
            result.add(root.val);
            preorderTraversalTailRecursion(root.left, result);
            preorderTraversalTailRecursion(root.right, result);
        }
    }

    public static ArrayList<Integer> preorderTraversalIteration(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        Stack<TreeNode> path = new Stack<TreeNode>();
        HashSet<TreeNode> visitedNodes = new HashSet<TreeNode>();

        if (root == null) {
            return result;
        }

        TreeNode node = root;
        while (true) {
            if (!visitedNodes.contains(node)) {
                visitedNodes.add(node);
                result.add(node.val);
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
        return result;
    }

    public static void main(String []args){
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(3);
        root.left.right = new TreeNode(4);
        root.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);

        long start;
        ArrayList<Integer> result;

        start = System.nanoTime();
        result = preorderTraversalRecursion(root);
        System.out.println("recursion method cost " + TimeUnit.NANOSECONDS.toMillis(System.nanoTime()-start) + " ms");
        System.out.println(result);

        result = new ArrayList<Integer>();
        start = System.nanoTime();
        preorderTraversalTailRecursion(root, result);
        System.out.println("tail-recursion method cost " + TimeUnit.NANOSECONDS.toMillis(System.nanoTime()-start) + " ms");
        System.out.println(result);

        start = System.nanoTime();
        result = preorderTraversalIteration(root);
        System.out.println("iteration method cost " + TimeUnit.NANOSECONDS.toMillis(System.nanoTime()-start) + " ms");
        System.out.println(result);
    }
}
