package tree;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Stack;
import java.util.concurrent.TimeUnit;

/*
 * http://oj.leetcode.com/problems/binary-tree-postOrder-traversal/
 */
public class PostorderTraversal {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public static ArrayList<Integer> postOrderTraversalRecursion(TreeNode root) {
        if (root == null) {
            return new ArrayList<Integer>();
        } else {
            ArrayList<Integer> result = new ArrayList<Integer>();
            result.addAll(postOrderTraversalRecursion(root.left));
            result.addAll(postOrderTraversalRecursion(root.right));
            result.add(root.val);
            return result;
        }
    }

    public static void postOrderTraversalTailRecursion(TreeNode root, ArrayList<Integer> result) {
        if (root != null) {
            postOrderTraversalTailRecursion(root.left, result);
            postOrderTraversalTailRecursion(root.right, result);
            result.add(root.val);
        }
    }

    public static ArrayList<Integer> postOrderTraversalIteration(TreeNode root) {
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
            } else if (node.right != null && !visitedNodes.contains(node.right)) {
                path.push(node);
                node = node.right;
            } else {
                if (!visitedNodes.contains(node)) {
                    visitedNodes.add(node);
                    result.add(node.val);
                }

                if (!path.isEmpty()) {
                    node = path.pop();
                } else {
                    break;
                }
            }
        }
        return result;
    }

    public static void main(String []args){
        TreeNode root = new TreeNode(1);
        root.right = new TreeNode(2);
        root.right.left = new TreeNode(3);

        long start;
        ArrayList<Integer> result;

        start = System.nanoTime();
        result = postOrderTraversalRecursion(root);
        System.out.println("recursion method cost " + TimeUnit.NANOSECONDS.toMillis(System.nanoTime()-start) + " ms");
        System.out.println(result);

        result = new ArrayList<Integer>();
        start = System.nanoTime();
        postOrderTraversalTailRecursion(root, result);
        System.out.println("tail-recursion method cost " + TimeUnit.NANOSECONDS.toMillis(System.nanoTime()-start) + " ms");
        System.out.println(result);

        start = System.nanoTime();
        result = postOrderTraversalIteration(root);
        System.out.println("iteration method cost " + TimeUnit.NANOSECONDS.toMillis(System.nanoTime()-start) + " ms");
        System.out.println(result);
    }
}
