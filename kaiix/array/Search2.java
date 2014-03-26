package array;

/*
 * http://oj.leetcode.com/problems/search-in-rotated-sorted-array-ii/
 */

public class Search2 {

    public static boolean search(int[] A, int target) {
        if (A.length == 0) {
            return false;
        }
        if (A.length == 1) {
            return A[0] == target;
        }
        int start = 0;
        for (int i = 0; i < A.length-1; i++) {
            if (A[i] != A[i+1]) {
                start = i;
                break;
            }
        }
        int end = 0;
        if (A[start] > A[start+1]) {
            end = start;
        } else {
            end = findEndOfArray(A, start+1, A.length-1);
        }
        if (target > A[0]) {
            return search(A, 1, end, target) != -1;
        } else if (target < A[0]){
            return search(A, end+1, A.length-1, target) != -1;
        } else {
            return true;
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

    static int findEndOfArray(int[] A, int p, int q) {
        if (p == q) {
            return p;
        }
        
        if (p > q) {
            return -1;
        }
        
        int mid = (p + q) / 2;
        if (A[mid] > A[0]) {
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
        System.out.println("result = " + search(new int[] {1}, 1));
        System.out.println("result = " + search(new int[] {1}, 2));
        System.out.println("result = " + search(new int[] {1, 2}, 2));
        System.out.println("result = " + search(new int[] {1, 3, 1, 1, 1}, 1));
        System.out.println("result = " + search(new int[] {1, 3, 1, 1, 1}, 3));
        System.out.println("result = " + search(new int[] {3, 1}, 3));
        System.out.println("result = " + search(new int[] {3, 1}, 1));
        System.out.println("result = " + search(new int[] {1, 1, 1, 1, 1, 1, 3, 1, 1, 1}, 3));
    }   
}
