package array;

/*
 * http://oj.leetcode.com/problems/search-in-rotated-sorted-array/
 */

public class Search {
    public static int search(int[] A, int target) {
        int end = findEndOfArray(A, 0, A.length-1);
        System.out.println("end = " + end);
        if (target > A[0]) {
            return search(A, 1, end, target);
        } else if (target < A[0]) {
            return search(A, end+1, A.length-1, target);
        } else {
            return 0;
        }
    }
    
    static int search(int[] A, int p, int q, int target) {
        if (p > q) {
            return -1;
        }
        
        int m = (p + q) / 2;
        if (target > A[m]) {
            return search(A, m+1, q, target);
        } else if (target < A[m]){
            return search(A, p, m-1, target);
        } else {
            return m;
        }
    }
    
    public static int findEndOfArray(int[] A, int p, int q) {
        if (p > q) {
            return -1;
        } else if (p == q) {
            return p;
        }
        
        int mid = (p + q) / 2;
        if (A[mid] >= A[0]) {
            if (A[mid] > A[mid+1]) {
                return mid;
            } else {
                return findEndOfArray(A, mid+1, q);
            }
        } else {
            return findEndOfArray(A, p, mid-1);
        }
    }
    
    public static void main(String []args){
        System.out.println("result = " + search(new int[] {5, 8, 9, 10, 1, 2, 3}, 3));
        System.out.println("result = " + search(new int[] {5, 8, 9, 10, 2, 3}, 3));
        System.out.println("result = " + search(new int[] {1, 2}, 1));
        System.out.println("result = " + search(new int[] {1, 2}, 2));
        System.out.println("result = " + search(new int[] {1}, 1));
        System.out.println("result = " + search(new int[] {1}, 2));
    }   
}
