package array;

/*
 * http://oj.leetcode.com/problems/median-of-two-sorted-arrays/
 */

public class FindMedianSortedArrays {
    public static double findMedianSortedArrays(int A[], int B[]) {
        int totalLength = A.length + B.length;
        int medianIndex = (totalLength + totalLength % 2) / 2;
        // find kth minimum number (which k this time equals to medianIndex)
        int i = 0, j = 0, min = 0;
        while (medianIndex > 0) {
            if (A.length == i) {
                min = B[j++];
            } else if (B.length == j) {
                min = A[i++];
            } else {
                min = A[i] < B[j] ? A[i++] : B[j++];
            }
            medianIndex--;
        }

        if (totalLength % 2 == 0) {
            if (A.length == i) {
                min += B[j];
            } else if (B.length == j) {
                min += A[i];
            } else {
                min += A[i] < B[j] ? A[i++] : B[j++];
            }
            return min / 2.0;
        } else {
            return min;
        }
    }
    
    public static void main(String []args){
        System.out.println(findMedianSortedArrays(new int[]{1, 2, 3}, new int[]{4, 5, 6}));
        System.out.println(findMedianSortedArrays(new int[]{2}, new int[]{4, 5, 6}));
        System.out.println(findMedianSortedArrays(new int[]{2, 5}, new int[]{4}));
        System.out.println(findMedianSortedArrays(new int[]{2, 3}, new int[]{7}));
        System.out.println(findMedianSortedArrays(new int[]{2, 3}, new int[]{}));
        System.out.println(findMedianSortedArrays(new int[]{2}, new int[]{}));
        System.out.println(findMedianSortedArrays(new int[]{1}, new int[]{1, 2, 3}));
    }   
}
