package array;

/*
 * http://oj.leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
 */

public class RemoveDuplicates2 {
    
    public static int removeDuplicates(int[] A) {
        if (A.length < 2) return A.length;
        int p = A[0]-1, freePos = 0, dupCount = 0;
        for (int i = 0; i < A.length; i++) {
            if (A[i] == p) {
                if (dupCount < 1) {
                    dupCount++;
                    A[freePos++] = p;
                }
            } else {
                p = A[i];
                dupCount = 0;
                A[freePos++] = p;
            }
        }
        return freePos;
    }

    public static void main(String []args){
        int[] A;
        int len;
        
        A = new int[] {1, 1};
        len = removeDuplicates(A);
        printArray(A, len);

        A = new int[] {1, 1, 1, 1, 3, 3};
        len = removeDuplicates(A);
        printArray(A, len);

        A = new int[] {1, 1, 2, 3, 3, 4, 4, 4, 4, 5};
        len = removeDuplicates(A);
        printArray(A, len);
    }

    private static void printArray(int[] A, int len) {
        for (int i = 0; i < len; i++) {
            System.out.print(A[i] + " ");
        }
        System.out.println();
    }   
}
