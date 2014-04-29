package tree;

/*
 * http://oj.leetcode.com/problems/unique-binary-search-trees/
 */
public class NumTrees {
    public static int numTrees(int n) {
        if (n < 3) {
            return n;
        } else {
            return numTreesInRange(1, n);
        }
    }

    static int numTreesInRange(int p, int q) {
        if (p >= q) {
            return 1;
        } else {
            int sum = 0;
            for (int root = p; root <= q; root++) {
                sum += numTreesInRange(p, root - 1) * numTreesInRange(root + 1, q);
            }
            return sum;
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i < 12; i++)
            System.out.println(numTrees());
    }
}
