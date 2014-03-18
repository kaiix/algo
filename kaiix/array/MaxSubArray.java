package array;

/*
 * http://oj.leetcode.com/problems/maximum-subarray/
 */

public class MaxSubArray {
    public static int maxSubArray(int[] A) {
        if (A.length == 0) return A[0];
        int sum = 0, max = A[0];
        for (int i = 0; i < A.length; i++) {
            sum += A[i];
            max = Math.max(max, sum);
            if (sum < 0) {
                sum = 0;
            }
        }
        return max;
    }
    
    public static void main(String []args){
        System.out.println(maxSubArray(new int[] {-2, 1, -3, 4, -1, 2, 1, -5, 4}));
        System.out.println(maxSubArray(new int[] {-2, 2}));
        System.out.println(maxSubArray(new int[] {-2, 2, 3, 4, 5}));
        System.out.println(maxSubArray(new int[] {2, -1, 2, -1, -1, 2}));
        System.out.println(maxSubArray(new int[] {-1, -2, -3}));
        System.out.println(maxSubArray(new int[] {-2, -1}));
    }   
}
