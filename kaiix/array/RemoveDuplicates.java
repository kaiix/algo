package array;

/*
 * http://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/
 */

public class RemoveDuplicates {
    
    public static int removeDuplicates(int[] A) {
        if (A.length < 2) return A.length;
        int p = A[0], cnt = 1;
        for (int i = 1; i < A.length; i++) {
            if (A[i] != p) {
                p = A[i];
                A[cnt++] = p;
            }
        }
        return cnt;
    }

    public static void main(String []args){
        int[] A;
        
        A = new int[] {1, 1, 2};
        int len = removeDuplicates(A);
        for (int i = 0; i < len; i++) {
            System.out.print(A[i] + " ");
        }
        System.out.println();

        A = new int[] {1, 1, 2, 3, 3};
        len = removeDuplicates(A);
        for (int i = 0; i < len; i++) {
            System.out.print(A[i] + " ");
        }
    }   
}
